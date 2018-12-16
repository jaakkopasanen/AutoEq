# Campfire Audio Andromeda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.3; 28 0.9; 31 0.6; 34 0.4; 37 0.2; 41 -0.1; 45 -0.4; 49 -0.6; 54 -0.9; 60 -1.2; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.6; 96 -3.0; 106 -3.4; 116 -3.7; 128 -4.0; 141 -4.2; 155 -4.3; 170 -4.4; 187 -4.3; 206 -4.3; 227 -4.2; 249 -4.1; 274 -4.2; 302 -4.2; 332 -4.0; 365 -3.7; 402 -3.4; 442 -3.1; 486 -2.8; 535 -2.4; 588 -1.9; 647 -1.5; 712 -1.1; 783 -0.5; 861 -0.2; 947 -0.1; 1042 -0.1; 1146 -0.2; 1261 -0.5; 1387 -0.7; 1526 -0.7; 1678 -0.3; 1846 0.4; 2031 1.4; 2234 2.7; 2457 3.9; 2703 4.6; 2973 4.7; 3270 4.8; 3597 5.1; 3957 3.8; 4353 1.7; 4788 2.1; 5267 3.0; 5793 0.6; 6373 -0.7; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.0; 15026 -2.5; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  1.04 | 2.3 dB  |
| Peaking | 127 Hz   |  0.76 | -3.0 dB |
| Peaking | 312 Hz   |  0.7  | -3.3 dB |
| Peaking | 3176 Hz  |  1.57 | 5.5 dB  |
| Peaking | 14874 Hz |  4.36 | -2.9 dB |
| Peaking | 976 Hz   |  1.48 | 1.9 dB  |
| Peaking | 1399 Hz  |  0.81 | -1.9 dB |
| Peaking | 2361 Hz  |  3.18 | 1.7 dB  |
| Peaking | 5302 Hz  |  8.15 | 2.0 dB  |
| Peaking | 6125 Hz  | 12.03 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)