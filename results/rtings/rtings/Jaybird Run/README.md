# Jaybird Run

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.3; 28 -1.3; 31 -1.3; 34 -1.3; 37 -1.3; 41 -1.3; 45 -1.3; 49 -1.3; 54 -1.4; 60 -1.7; 66 -2.1; 72 -2.3; 79 -2.6; 87 -3.0; 96 -3.3; 106 -3.7; 116 -4.0; 128 -4.4; 141 -4.8; 155 -5.3; 170 -5.5; 187 -5.6; 206 -5.3; 227 -5.0; 249 -4.5; 274 -4.0; 302 -3.6; 332 -3.1; 365 -2.6; 402 -2.1; 442 -1.5; 486 -0.9; 535 -0.2; 588 0.4; 647 1.0; 712 1.5; 783 1.6; 861 1.3; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.9; 1387 -2.1; 1526 -2.5; 1678 -3.0; 1846 -3.7; 2031 -4.4; 2234 -4.7; 2457 -4.5; 2703 -3.5; 2973 -1.8; 3270 -0.2; 3597 1.1; 3957 1.9; 4353 2.4; 4788 3.1; 5267 3.4; 5793 1.7; 6373 -4.3; 7010 -8.9; 7711 -4.4; 8482 -1.6; 9330 -5.5; 10263 -6.9; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 167 Hz   | 0.75 | -5.7 dB  |
| Peaking | 2254 Hz  | 1.63 | -6.2 dB  |
| Peaking | 5711 Hz  | 1.09 | 18.3 dB  |
| Peaking | 6728 Hz  | 1.41 | -22.0 dB |
| Peaking | 24000 Hz | 2.03 | -3.6 dB  |
| Peaking | 26 Hz    | 0.66 | -1.1 dB  |
| Peaking | 738 Hz   | 2.98 | 2.6 dB   |
| Peaking | 8339 Hz  | 6.41 | 4.3 dB   |
| Peaking | 10030 Hz | 3.64 | -7.9 dB  |
| Peaking | 11466 Hz | 2.29 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20Run/Jaybird%20Run.png)