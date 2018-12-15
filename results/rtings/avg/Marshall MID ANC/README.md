# Marshall MID ANC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -3.8; 23 -3.5; 25 -3.4; 28 -3.3; 31 -3.3; 34 -3.3; 37 -3.2; 41 -3.2; 45 -3.3; 49 -3.5; 54 -3.6; 60 -3.7; 66 -3.8; 72 -3.9; 79 -4.0; 87 -4.1; 96 -4.1; 106 -4.0; 116 -3.8; 128 -3.6; 141 -3.4; 155 -3.2; 170 -2.8; 187 -2.5; 206 -2.1; 227 -1.7; 249 -1.4; 274 -1.2; 302 -0.9; 332 -0.6; 365 -0.4; 402 -0.2; 442 -0.2; 486 -0.2; 535 -0.3; 588 -0.3; 647 -0.2; 712 -0.2; 783 -0.2; 861 -0.2; 947 -0.1; 1042 0.0; 1146 -0.0; 1261 -0.7; 1387 -1.0; 1526 -0.9; 1678 -1.9; 1846 -2.1; 2031 -2.4; 2234 -2.1; 2457 -2.1; 2703 -2.9; 2973 -4.7; 3270 -6.6; 3597 -7.0; 3957 -8.2; 4353 -7.8; 4788 -3.3; 5267 -0.1; 5793 1.0; 6373 -3.8; 7010 -8.0; 7711 -8.9; 8482 -4.2; 9330 0.0; 10263 0.0; 11289 -5.8; 12418 -12.0; 13660 -13.2; 15026 -9.9; 16529 -4.8; 18182 -1.2; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall MID ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall MID ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.18 | -3.3 dB  |
| Peaking | 112 Hz   | 0.74 | -2.9 dB  |
| Peaking | 3724 Hz  | 1.72 | -7.6 dB  |
| Peaking | 13648 Hz | 1.86 | -14.1 dB |
| Peaking | 24000 Hz | 1.83 | -11.6 dB |
| Peaking | 1813 Hz  | 4.91 | -1.3 dB  |
| Peaking | 4251 Hz  | 9.73 | -4.0 dB  |
| Peaking | 5732 Hz  | 2.27 | 8.4 dB   |
| Peaking | 7321 Hz  | 2.01 | -11.7 dB |
| Peaking | 9533 Hz  | 3.17 | 7.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Marshall%20MID%20ANC/Marshall%20MID%20ANC.png)