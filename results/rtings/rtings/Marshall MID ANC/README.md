# Marshall MID ANC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 -3.8; 23 -3.5; 25 -3.4; 28 -3.3; 31 -3.3; 34 -3.3; 37 -3.2; 41 -3.2; 45 -3.3; 49 -3.5; 54 -3.6; 60 -3.7; 66 -3.8; 72 -3.9; 79 -4.0; 87 -4.1; 96 -4.1; 106 -4.0; 116 -3.8; 128 -3.6; 141 -3.4; 155 -3.2; 170 -2.8; 187 -2.5; 206 -2.1; 227 -1.7; 249 -1.4; 274 -1.2; 302 -0.9; 332 -0.6; 365 -0.4; 402 -0.2; 442 -0.2; 486 -0.2; 535 -0.3; 588 -0.3; 647 -0.2; 712 -0.2; 783 -0.2; 861 -0.2; 947 -0.1; 1042 0.0; 1146 -0.0; 1261 -0.7; 1387 -1.0; 1526 -0.9; 1678 -1.9; 1846 -2.1; 2031 -2.4; 2234 -2.1; 2457 -2.0; 2703 -2.6; 2973 -4.2; 3270 -5.9; 3597 -6.0; 3957 -7.0; 4353 -6.5; 4788 -1.5; 5267 2.5; 5793 3.5; 6373 -2.5; 7010 -7.1; 7711 -7.5; 8482 -3.5; 9330 -0.0; 10263 -0.3; 11289 -5.0; 12418 -8.8; 13660 -9.9; 15026 -7.3; 16529 -1.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall MID ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall MID ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.21 | -3.3 dB  |
| Peaking | 111 Hz   | 0.72 | -3.0 dB  |
| Peaking | 3576 Hz  | 1.95 | -6.6 dB  |
| Peaking | 13484 Hz | 1.94 | -10.6 dB |
| Peaking | 24000 Hz | 1.97 | -8.3 dB  |
| Peaking | 1845 Hz  | 3.8  | -1.5 dB  |
| Peaking | 4249 Hz  | 8.57 | -4.8 dB  |
| Peaking | 5677 Hz  | 2.67 | 9.7 dB   |
| Peaking | 7217 Hz  | 2.25 | -10.7 dB |
| Peaking | 9531 Hz  | 3.46 | 5.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Marshall%20MID%20ANC/Marshall%20MID%20ANC.png)