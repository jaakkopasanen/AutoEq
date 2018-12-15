# Campfire Audio Andromeda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.2; 72 4.4; 79 3.5; 87 2.5; 96 1.5; 106 0.6; 116 -0.3; 128 -1.2; 141 -1.9; 155 -2.6; 170 -3.2; 187 -3.6; 206 -4.0; 227 -4.3; 249 -4.4; 274 -4.6; 302 -4.5; 332 -4.1; 365 -3.8; 402 -3.4; 442 -3.1; 486 -2.7; 535 -2.3; 588 -1.8; 647 -1.3; 712 -0.9; 783 -0.4; 861 -0.1; 947 -0.0; 1042 -0.1; 1146 -0.1; 1261 -0.2; 1387 -0.0; 1526 0.2; 1678 0.6; 1846 1.5; 2031 2.8; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.6; 4788 3.8; 5267 4.6; 5793 2.6; 6373 1.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.0; 15026 -18.0; 16529 -17.7; 18182 -11.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 52 Hz    |  0.32 | 8.3 dB   |
| Peaking | 188 Hz   |  0.46 | -7.8 dB  |
| Peaking | 3623 Hz  |  0.78 | 7.2 dB   |
| Peaking | 12028 Hz |  1.31 | 11.7 dB  |
| Peaking | 15486 Hz |  1.03 | -25.0 dB |
| Peaking | 835 Hz   |  2.04 | 1.0 dB   |
| Peaking | 1645 Hz  |  1.35 | -1.7 dB  |
| Peaking | 2409 Hz  |  3.49 | 2.4 dB   |
| Peaking | 4425 Hz  | 10.33 | -1.8 dB  |
| Peaking | 6825 Hz  | 12.61 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)