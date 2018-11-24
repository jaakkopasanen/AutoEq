# Denon AH-D7000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.1; 34 4.1; 37 3.2; 41 2.5; 45 2.2; 49 2.0; 54 1.6; 60 1.6; 66 1.6; 72 1.4; 79 1.4; 87 1.3; 96 1.3; 106 1.5; 116 1.6; 128 1.6; 141 1.6; 155 1.6; 170 2.0; 187 2.1; 206 2.3; 227 2.8; 249 3.2; 274 3.7; 302 4.2; 332 4.6; 365 5.0; 402 4.6; 442 4.2; 486 2.7; 535 1.3; 588 0.5; 647 -0.0; 712 -0.7; 783 -0.6; 861 0.5; 947 0.4; 1042 -0.1; 1146 0.5; 1261 1.0; 1387 1.1; 1526 1.3; 1678 1.7; 1846 2.3; 2031 2.6; 2234 2.9; 2457 3.8; 2703 4.5; 2973 4.8; 3270 4.4; 3597 3.5; 3957 2.4; 4353 -0.4; 4788 0.7; 5267 1.8; 5793 0.8; 6373 -0.0; 7010 0.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.6; 11289 -1.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.78 | 6.2 dB  |
| Peaking | 235 Hz   | 1.04 | 2.3 dB  |
| Peaking | 377 Hz   | 2.46 | 4.1 dB  |
| Peaking | 2023 Hz  | 2.07 | 1.6 dB  |
| Peaking | 3014 Hz  | 2.24 | 4.7 dB  |
| Peaking | 455 Hz   | 8.41 | 1.0 dB  |
| Peaking | 705 Hz   | 3.67 | -1.5 dB |
| Peaking | 4432 Hz  | 6.67 | -3.9 dB |
| Peaking | 4596 Hz  | 2.81 | 2.1 dB  |
| Peaking | 10745 Hz | 6.51 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)