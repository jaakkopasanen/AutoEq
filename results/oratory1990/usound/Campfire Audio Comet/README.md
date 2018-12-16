# Campfire Audio Comet

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.6; 28 2.4; 31 2.2; 34 2.1; 37 2.0; 41 1.8; 45 1.6; 49 1.4; 54 1.2; 60 0.9; 66 0.6; 72 0.3; 79 -0.1; 87 -0.6; 96 -1.0; 106 -1.4; 116 -1.8; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.7; 187 -2.9; 206 -2.9; 227 -2.9; 249 -3.0; 274 -3.3; 302 -3.5; 332 -3.3; 365 -3.1; 402 -2.9; 442 -2.7; 486 -2.4; 535 -2.1; 588 -1.8; 647 -1.4; 712 -0.9; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 0.0; 1387 0.2; 1526 0.7; 1678 1.4; 1846 2.2; 2031 2.7; 2234 2.7; 2457 2.2; 2703 0.8; 2973 -1.4; 3270 -2.4; 3597 -0.5; 3957 2.1; 4353 4.0; 4788 5.0; 5267 4.9; 5793 3.7; 6373 0.7; 7010 -2.5; 7711 -2.2; 8482 -1.4; 9330 -1.3; 10263 -1.3; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.39 | 2.9 dB  |
| Peaking | 243 Hz  | 0.52 | -3.5 dB |
| Peaking | 2013 Hz | 3.14 | 3.1 dB  |
| Peaking | 5207 Hz | 2.78 | 6.9 dB  |
| Peaking | 7331 Hz | 1.8  | -3.5 dB |
| Peaking | 120 Hz  | 3.96 | -0.3 dB |
| Peaking | 2010 Hz | 3.55 | -2.1 dB |
| Peaking | 2402 Hz | 1.46 | 2.7 dB  |
| Peaking | 3202 Hz | 3.17 | -4.7 dB |
| Peaking | 4213 Hz | 5.89 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)