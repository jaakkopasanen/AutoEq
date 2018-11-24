# Jaybird Freedom

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -1.5; 23 -1.5; 25 -1.5; 28 -1.5; 31 -1.5; 34 -1.5; 37 -1.5; 41 -1.5; 45 -1.5; 49 -1.5; 54 -1.5; 60 -1.9; 66 -2.2; 72 -2.5; 79 -2.8; 87 -3.1; 96 -3.5; 106 -4.0; 116 -4.4; 128 -4.8; 141 -5.0; 155 -5.1; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.9; 249 -5.3; 274 -5.1; 302 -4.6; 332 -4.0; 365 -3.5; 402 -3.0; 442 -2.5; 486 -2.0; 535 -1.4; 588 -0.8; 647 -0.2; 712 0.4; 783 0.8; 861 0.8; 947 0.4; 1042 -0.3; 1146 -1.3; 1261 -2.3; 1387 -3.2; 1526 -3.5; 1678 -3.9; 1846 -4.2; 2031 -4.8; 2234 -5.1; 2457 -5.4; 2703 -5.8; 2973 -4.7; 3270 -2.6; 3597 -0.8; 3957 0.4; 4353 1.0; 4788 2.5; 5267 4.0; 5793 3.9; 6373 0.8; 7010 -2.2; 7711 -4.6; 8482 -4.9; 9330 -4.4; 10263 -4.0; 11289 -4.2; 12418 -3.0; 13660 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.19 | -1.2 dB |
| Peaking | 195 Hz   | 0.71 | -4.9 dB |
| Peaking | 2430 Hz  | 1.29 | -6.3 dB |
| Peaking | 5613 Hz  | 1.49 | 9.5 dB  |
| Peaking | 7914 Hz  | 1.11 | -8.4 dB |
| Peaking | 361 Hz   | 1.92 | -0.9 dB |
| Peaking | 831 Hz   | 1.74 | 2.2 dB  |
| Peaking | 1386 Hz  | 2.95 | -1.7 dB |
| Peaking | 11890 Hz | 3.59 | -3.4 dB |
| Peaking | 13205 Hz | 1.57 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20Freedom/Jaybird%20Freedom.png)