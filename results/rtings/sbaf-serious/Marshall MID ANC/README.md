# Marshall MID ANC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 -3.4; 23 -3.2; 25 -3.1; 28 -3.2; 31 -3.2; 34 -3.3; 37 -3.3; 41 -3.5; 45 -3.6; 49 -3.8; 54 -4.0; 60 -4.0; 66 -4.0; 72 -3.9; 79 -3.8; 87 -3.7; 96 -3.6; 106 -3.5; 116 -3.3; 128 -3.1; 141 -2.8; 155 -2.5; 170 -2.2; 187 -1.9; 206 -1.6; 227 -1.3; 249 -0.8; 274 -0.6; 302 -0.1; 332 0.4; 365 0.6; 402 0.8; 442 1.0; 486 1.0; 535 0.9; 588 0.8; 647 0.8; 712 0.7; 783 0.2; 861 -0.0; 947 -0.1; 1042 0.1; 1146 0.2; 1261 -0.4; 1387 -1.0; 1526 -1.2; 1678 -2.3; 1846 -2.1; 2031 -2.0; 2234 -1.6; 2457 -1.6; 2703 -2.0; 2973 -3.1; 3270 -4.0; 3597 -3.8; 3957 -5.8; 4353 -6.5; 4788 -1.7; 5267 2.9; 5793 4.9; 6373 0.0; 7010 -4.6; 7711 -6.4; 8482 -3.2; 9330 0.0; 10263 0.0; 11289 -0.7; 12418 -4.3; 13660 -6.1; 15026 -4.0; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall MID ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall MID ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.44 | -4.3 dB  |
| Peaking | 4392 Hz  | 1.13 | -19.9 dB |
| Peaking | 5482 Hz  | 1.07 | 21.3 dB  |
| Peaking | 7382 Hz  | 2.86 | -11.7 dB |
| Peaking | 13624 Hz | 2.59 | -7.9 dB  |
| Peaking | 16 Hz    | 2.18 | -1.2 dB  |
| Peaking | 167 Hz   | 1.21 | -0.8 dB  |
| Peaking | 458 Hz   | 0.9  | 1.5 dB   |
| Peaking | 1683 Hz  | 4.32 | -1.1 dB  |
| Peaking | 1848 Hz  | 4.85 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Marshall%20MID%20ANC/Marshall%20MID%20ANC.png)