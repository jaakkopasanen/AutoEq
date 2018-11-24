# Rovking V1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -15.6; 23 -15.6; 25 -15.5; 28 -15.5; 31 -15.4; 34 -15.4; 37 -15.3; 41 -15.2; 45 -15.2; 49 -15.1; 54 -15.1; 60 -15.0; 66 -15.0; 72 -14.9; 79 -14.9; 87 -14.8; 96 -14.7; 106 -14.7; 116 -14.6; 128 -14.4; 141 -14.0; 155 -13.5; 170 -12.9; 187 -12.1; 206 -11.5; 227 -11.0; 249 -10.6; 274 -10.0; 302 -9.3; 332 -8.4; 365 -7.4; 402 -6.4; 442 -5.3; 486 -4.2; 535 -3.2; 588 -2.2; 647 -1.6; 712 -1.3; 783 -0.9; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.7; 1387 0.7; 1526 1.0; 1678 1.7; 1846 2.4; 2031 3.2; 2234 3.8; 2457 3.5; 2703 2.9; 2973 1.4; 3270 0.1; 3597 -0.9; 3957 -2.2; 4353 -3.7; 4788 -5.5; 5267 -4.4; 5793 -2.7; 6373 -2.4; 7010 -2.1; 7711 -5.6; 8482 -5.4; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 -3.9; 13660 -4.3; 15026 -2.5; 16529 -1.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rovking V1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rovking V1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.18 | -15.2 dB |
| Peaking | 184 Hz   | 0.63 | -6.4 dB  |
| Peaking | 4889 Hz  | 4.36 | -5.9 dB  |
| Peaking | 8017 Hz  | 5.61 | -6.5 dB  |
| Peaking | 13499 Hz | 3.26 | -4.9 dB  |
| Peaking | 361 Hz   | 1.62 | -2.3 dB  |
| Peaking | 626 Hz   | 0.4  | 1.1 dB   |
| Peaking | 2406 Hz  | 1.54 | 5.5 dB   |
| Peaking | 3316 Hz  | 0.94 | -2.3 dB  |
| Peaking | 10309 Hz | 4.31 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Rovking%20V1/Rovking%20V1.png)