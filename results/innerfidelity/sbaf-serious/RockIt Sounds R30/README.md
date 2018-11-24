# RockIt Sounds R30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.6; 41 5.2; 45 4.9; 49 4.6; 54 4.3; 60 3.8; 66 3.4; 72 3.0; 79 2.6; 87 2.0; 96 1.5; 106 1.2; 116 1.0; 128 0.5; 141 0.2; 155 -0.0; 170 -0.2; 187 -0.4; 206 -0.5; 227 -0.5; 249 -0.6; 274 -0.6; 302 -0.5; 332 -0.4; 365 -0.4; 402 -0.2; 442 0.0; 486 0.0; 535 0.2; 588 0.6; 647 0.7; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.4; 1526 -1.8; 1678 -2.0; 1846 -1.6; 2031 -0.9; 2234 0.1; 2457 2.0; 2703 3.9; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RockIt Sounds R30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RockIt Sounds R30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 6.2 dB  |
| Peaking | 183 Hz  | 0.54 | -1.3 dB |
| Peaking | 716 Hz  | 1.47 | 1.0 dB  |
| Peaking | 1767 Hz | 1.55 | -4.2 dB |
| Peaking | 3875 Hz | 0.93 | 7.4 dB  |
| Peaking | 2967 Hz | 6.57 | 1.7 dB  |
| Peaking | 3989 Hz | 3.39 | -0.9 dB |
| Peaking | 6346 Hz | 2.24 | 4.9 dB  |
| Peaking | 7300 Hz | 0.69 | -1.4 dB |
| Peaking | 7487 Hz | 2.74 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RockIt%20Sounds%20R30/RockIt%20Sounds%20R30.png)