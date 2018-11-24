# Sennheiser IE 80 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.8; 28 -10.8; 31 -10.9; 34 -10.9; 37 -10.9; 41 -11.0; 45 -11.0; 49 -11.1; 54 -11.2; 60 -11.3; 66 -11.5; 72 -11.6; 79 -11.8; 87 -11.9; 96 -12.1; 106 -12.2; 116 -12.2; 128 -12.2; 141 -12.1; 155 -11.9; 170 -11.7; 187 -11.3; 206 -10.9; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.7; 332 -8.0; 365 -7.2; 402 -6.6; 442 -5.9; 486 -5.1; 535 -4.3; 588 -3.6; 647 -2.8; 712 -2.0; 783 -1.3; 861 -0.7; 947 -0.2; 1042 0.0; 1146 0.1; 1261 0.3; 1387 0.5; 1526 0.5; 1678 0.4; 1846 0.5; 2031 1.0; 2234 1.5; 2457 1.7; 2703 1.5; 2973 1.0; 3270 0.3; 3597 -0.5; 3957 -1.7; 4353 -3.7; 4788 -6.7; 5267 -6.6; 5793 -1.9; 6373 1.8; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 -3.3; 13660 -9.4; 15026 -14.4; 16529 -16.2; 18182 -15.5; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.2  | -10.4 dB |
| Peaking | 157 Hz   | 0.68 | -6.5 dB  |
| Peaking | 340 Hz   | 1.18 | -3.6 dB  |
| Peaking | 4949 Hz  | 6.69 | -7.7 dB  |
| Peaking | 17399 Hz | 1.24 | -18.6 dB |
| Peaking | 1126 Hz  | 1.12 | 2.7 dB   |
| Peaking | 2645 Hz  | 0.9  | 6.4 dB   |
| Peaking | 5495 Hz  | 0.18 | -5.7 dB  |
| Peaking | 6836 Hz  | 2.61 | 7.1 dB   |
| Peaking | 10720 Hz | 1.81 | 8.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)