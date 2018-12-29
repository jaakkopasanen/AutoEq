# Campfire Audio Comet

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.3; 28 2.1; 31 1.9; 34 1.8; 37 1.7; 41 1.5; 45 1.3; 49 1.1; 54 0.9; 60 0.6; 66 0.3; 72 -0.0; 79 -0.4; 87 -0.9; 96 -1.3; 106 -1.7; 116 -2.1; 128 -2.4; 141 -2.7; 155 -2.9; 170 -3.0; 187 -3.2; 206 -3.2; 227 -3.2; 249 -3.4; 274 -3.7; 302 -3.8; 332 -3.5; 365 -3.1; 402 -2.9; 442 -2.6; 486 -2.3; 535 -2.0; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.4; 861 -0.1; 947 0.0; 1042 0.0; 1146 0.1; 1261 0.4; 1387 0.9; 1526 1.6; 1678 2.4; 1846 3.2; 2031 4.0; 2234 4.6; 2457 4.7; 2703 3.7; 2973 1.7; 3270 0.7; 3597 2.3; 3957 4.5; 4353 5.9; 4788 6.0; 5267 6.0; 5793 5.7; 6373 3.0; 7010 0.7; 7711 0.3; 8482 0.0; 9330 -1.5; 10263 -2.8; 11289 -0.6; 12418 0.0; 13660 -0.3; 15026 -4.8; 16529 -7.5; 18182 -6.1; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.35 | 2.6 dB  |
| Peaking | 232 Hz   | 0.51 | -3.8 dB |
| Peaking | 2166 Hz  | 1.98 | 4.6 dB  |
| Peaking | 4988 Hz  | 2.25 | 6.8 dB  |
| Peaking | 17204 Hz | 1.38 | -7.9 dB |
| Peaking | 2676 Hz  | 5.21 | 1.3 dB  |
| Peaking | 3227 Hz  | 4.4  | -2.1 dB |
| Peaking | 4089 Hz  | 6.79 | 1.7 dB  |
| Peaking | 10057 Hz | 4.89 | -2.9 dB |
| Peaking | 12923 Hz | 3.75 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)