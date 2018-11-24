# Monoprice Enhanced Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.4; 28 1.8; 31 1.4; 34 1.0; 37 0.7; 41 0.3; 45 0.0; 49 -0.2; 54 -0.5; 60 -1.0; 66 -1.4; 72 -1.7; 79 -1.9; 87 -2.2; 96 -2.5; 106 -2.9; 116 -3.2; 128 -3.5; 141 -3.8; 155 -4.0; 170 -4.3; 187 -4.7; 206 -5.1; 227 -5.6; 249 -6.1; 274 -6.6; 302 -7.0; 332 -7.5; 365 -8.0; 402 -8.4; 442 -8.4; 486 -8.4; 535 -7.7; 588 -6.6; 647 -5.0; 712 -3.2; 783 -1.8; 861 -0.8; 947 -0.0; 1042 -0.1; 1146 -0.1; 1261 -0.3; 1387 -0.4; 1526 -0.5; 1678 -0.6; 1846 -0.6; 2031 -0.6; 2234 -0.2; 2457 0.4; 2703 0.2; 2973 -0.9; 3270 -2.7; 3597 -4.7; 3957 -7.1; 4353 -8.1; 4788 -5.4; 5267 -1.6; 5793 1.4; 6373 0.7; 7010 -0.4; 7711 -3.8; 8482 -7.9; 9330 -9.8; 10263 -8.1; 11289 -3.0; 12418 0.0; 13660 -1.5; 15026 -1.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.79 | 3.5 dB   |
| Peaking | 382 Hz  | 0.54 | -10.1 dB |
| Peaking | 1944 Hz | 0.14 | 2.8 dB   |
| Peaking | 4112 Hz | 2.68 | -10.4 dB |
| Peaking | 9395 Hz | 2.81 | -12.3 dB |
| Peaking | 541 Hz  | 3.33 | -1.9 dB  |
| Peaking | 886 Hz  | 2    | 2.2 dB   |
| Peaking | 1780 Hz | 2.35 | -1.6 dB  |
| Peaking | 6040 Hz | 1.3  | -2.1 dB  |
| Peaking | 6166 Hz | 3.38 | 4.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)