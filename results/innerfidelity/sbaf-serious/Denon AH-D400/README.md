# Denon AH-D400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.1; 34 4.5; 37 4.0; 41 3.5; 45 3.2; 49 2.9; 54 2.6; 60 2.2; 66 2.0; 72 1.7; 79 1.4; 87 1.1; 96 0.5; 106 0.0; 116 -0.3; 128 -0.7; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.6; 227 -1.5; 249 -1.5; 274 -1.5; 302 -1.1; 332 -0.5; 365 0.7; 402 2.1; 442 3.6; 486 4.6; 535 5.5; 588 5.8; 647 5.0; 712 3.5; 783 2.6; 861 1.4; 947 0.5; 1042 -0.2; 1146 -0.2; 1261 0.3; 1387 0.1; 1526 0.7; 1678 0.5; 1846 0.1; 2031 1.0; 2234 1.5; 2457 1.8; 2703 2.0; 2973 2.5; 3270 3.8; 3597 6.0; 3957 5.3; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.7  | 6.1 dB  |
| Peaking | 73 Hz   | 1.12 | 1.2 dB  |
| Peaking | 403 Hz  | 0.37 | -3.9 dB |
| Peaking | 553 Hz  | 1.28 | 9.5 dB  |
| Peaking | 4552 Hz | 1.2  | 6.7 dB  |
| Peaking | 1050 Hz | 7.5  | -0.7 dB |
| Peaking | 3582 Hz | 6.81 | 2.0 dB  |
| Peaking | 4151 Hz | 6.99 | -1.7 dB |
| Peaking | 6386 Hz | 3.27 | 4.4 dB  |
| Peaking | 7337 Hz | 1.61 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D400/Denon%20AH-D400.png)