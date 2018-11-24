# Monoprice Enhanced Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.7; 28 2.0; 31 1.4; 34 1.0; 37 0.6; 41 0.1; 45 -0.2; 49 -0.5; 54 -0.8; 60 -1.3; 66 -1.5; 72 -1.7; 79 -1.7; 87 -1.9; 96 -2.1; 106 -2.4; 116 -2.7; 128 -3.0; 141 -3.2; 155 -3.4; 170 -3.7; 187 -4.1; 206 -4.6; 227 -5.1; 249 -5.5; 274 -5.9; 302 -6.2; 332 -6.6; 365 -7.0; 402 -7.3; 442 -7.3; 486 -7.1; 535 -6.5; 588 -5.5; 647 -4.0; 712 -2.4; 783 -1.3; 861 -0.6; 947 -0.0; 1042 -0.0; 1146 0.1; 1261 -0.1; 1387 -0.4; 1526 -0.8; 1678 -0.9; 1846 -0.6; 2031 -0.2; 2234 0.3; 2457 0.8; 2703 0.8; 2973 0.2; 3270 -0.9; 3597 -2.6; 3957 -5.9; 4353 -8.1; 4788 -5.6; 5267 -1.1; 5793 2.8; 6373 3.3; 7010 2.1; 7711 -2.7; 8482 -7.6; 9330 -8.3; 10263 -4.7; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 2.18 | 3.7 dB   |
| Peaking | 339 Hz  | 0.64 | -7.2 dB  |
| Peaking | 4439 Hz | 2.16 | -16.4 dB |
| Peaking | 6146 Hz | 0.75 | 13.0 dB  |
| Peaking | 8852 Hz | 2.08 | -16.4 dB |
| Peaking | 91 Hz   | 0.99 | -0.9 dB  |
| Peaking | 296 Hz  | 1.38 | 1.1 dB   |
| Peaking | 533 Hz  | 1.44 | -3.8 dB  |
| Peaking | 795 Hz  | 0.87 | 3.1 dB   |
| Peaking | 1650 Hz | 2.47 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)