# Jaybird Freedom

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -1.5; 23 -1.5; 25 -1.5; 28 -1.5; 31 -1.5; 34 -1.5; 37 -1.5; 41 -1.5; 45 -1.5; 49 -1.5; 54 -1.5; 60 -1.9; 66 -2.2; 72 -2.5; 79 -2.8; 87 -3.1; 96 -3.5; 106 -4.0; 116 -4.4; 128 -4.8; 141 -5.0; 155 -5.1; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.9; 249 -5.3; 274 -5.1; 302 -4.6; 332 -4.0; 365 -3.5; 402 -3.0; 442 -2.5; 486 -2.0; 535 -1.4; 588 -0.8; 647 -0.2; 712 0.4; 783 0.8; 861 0.8; 947 0.4; 1042 -0.3; 1146 -1.3; 1261 -2.3; 1387 -3.2; 1526 -3.5; 1678 -3.9; 1846 -4.2; 2031 -4.8; 2234 -5.0; 2457 -5.5; 2703 -6.0; 2973 -5.2; 3270 -3.3; 3597 -1.9; 3957 -0.8; 4353 -0.3; 4788 0.7; 5267 1.4; 5793 1.5; 6373 -0.4; 7010 -3.1; 7711 -6.0; 8482 -5.6; 9330 -3.0; 10263 -2.2; 11289 -4.9; 12418 -6.3; 13660 -1.2; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.15 | -1.2 dB |
| Peaking | 195 Hz   | 0.69 | -4.9 dB |
| Peaking | 2320 Hz  | 1.59 | -5.9 dB |
| Peaking | 10682 Hz | 1.24 | -4.7 dB |
| Peaking | 24000 Hz | 2.03 | -3.8 dB |
| Peaking | 829 Hz   | 2.5  | 2.2 dB  |
| Peaking | 1410 Hz  | 3.02 | -1.7 dB |
| Peaking | 5498 Hz  | 2.71 | 3.3 dB  |
| Peaking | 7768 Hz  | 5.4  | -4.7 dB |
| Peaking | 14907 Hz | 4.69 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom/Jaybird%20Freedom.png)