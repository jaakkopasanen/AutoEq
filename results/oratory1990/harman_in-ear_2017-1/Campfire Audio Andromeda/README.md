# Campfire Audio Andromeda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.0; 28 0.6; 31 0.3; 34 0.0; 37 -0.2; 41 -0.4; 45 -0.7; 49 -0.9; 54 -1.2; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.6; 87 -3.0; 96 -3.4; 106 -3.7; 116 -4.0; 128 -4.3; 141 -4.5; 155 -4.6; 170 -4.7; 187 -4.6; 206 -4.6; 227 -4.5; 249 -4.4; 274 -4.5; 302 -4.5; 332 -4.1; 365 -3.8; 402 -3.4; 442 -3.1; 486 -2.7; 535 -2.3; 588 -1.8; 647 -1.3; 712 -0.9; 783 -0.4; 861 -0.1; 947 -0.0; 1042 -0.1; 1146 -0.1; 1261 -0.2; 1387 -0.0; 1526 0.2; 1678 0.6; 1846 1.5; 2031 2.8; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.6; 4788 3.8; 5267 4.6; 5793 2.6; 6373 1.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.0; 15026 -18.0; 16529 -17.7; 18182 -11.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.85 | 2.3 dB   |
| Peaking | 121 Hz   | 1.01 | -0.7 dB  |
| Peaking | 218 Hz   | 0.4  | -4.4 dB  |
| Peaking | 3634 Hz  | 0.67 | 6.2 dB   |
| Peaking | 16205 Hz | 1.76 | -21.0 dB |
| Peaking | 1612 Hz  | 1.46 | -5.3 dB  |
| Peaking | 1841 Hz  | 0.79 | 3.7 dB   |
| Peaking | 4416 Hz  | 5.54 | -2.2 dB  |
| Peaking | 11886 Hz | 3.08 | 6.5 dB   |
| Peaking | 18601 Hz | 0.31 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)