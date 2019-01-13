# Denon AH-D310R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.5; 28 3.9; 31 3.4; 34 3.0; 37 2.7; 41 2.3; 45 1.9; 49 1.6; 54 1.3; 60 0.8; 66 0.7; 72 0.9; 79 1.2; 87 0.4; 96 -0.2; 106 -0.4; 116 -0.6; 128 -0.8; 141 -1.1; 155 -1.5; 170 -2.4; 187 -2.8; 206 -2.6; 227 -2.6; 249 -2.2; 274 -1.8; 302 -0.3; 332 -0.0; 365 0.3; 402 1.1; 442 1.4; 486 2.0; 535 2.1; 588 2.7; 647 4.1; 712 5.1; 783 3.1; 861 0.5; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -0.5; 1526 5.8; 1678 2.2; 1846 5.2; 2031 4.7; 2234 3.5; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.3; 4788 3.3; 5267 6.0; 5793 4.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -2.1; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D310R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D310R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.12 | 5.4 dB  |
| Peaking | 678 Hz  |  3.93 | 5.1 dB  |
| Peaking | 1896 Hz |  3.52 | 3.3 dB  |
| Peaking | 3217 Hz |  1.49 | 6.3 dB  |
| Peaking | 5864 Hz |  3.39 | 4.7 dB  |
| Peaking | 206 Hz  |  1.59 | -3.1 dB |
| Peaking | 456 Hz  |  2.28 | 1.6 dB  |
| Peaking | 1350 Hz |  2.63 | -2.6 dB |
| Peaking | 1530 Hz | 11.54 | 6.0 dB  |
| Peaking | 9301 Hz |  5.37 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D310R/Denon%20AH-D310R.png)