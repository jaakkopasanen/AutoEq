# Focal Spirit One S 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.4; 28 -3.6; 31 -3.6; 34 -3.7; 37 -3.8; 41 -3.9; 45 -3.9; 49 -3.9; 54 -4.0; 60 -4.1; 66 -4.1; 72 -4.0; 79 -4.0; 87 -4.6; 96 -5.4; 106 -5.8; 116 -5.6; 128 -5.5; 141 -5.8; 155 -5.8; 170 -5.3; 187 -5.2; 206 -4.5; 227 -3.4; 249 -2.3; 274 -1.0; 302 0.3; 332 0.9; 365 0.6; 402 -0.1; 442 -0.9; 486 -1.5; 535 -1.5; 588 -1.0; 647 -1.0; 712 -0.9; 783 -0.2; 861 -0.1; 947 0.0; 1042 0.0; 1146 0.4; 1261 0.6; 1387 0.5; 1526 0.6; 1678 1.0; 1846 1.4; 2031 2.1; 2234 2.7; 2457 3.6; 2703 4.2; 2973 4.1; 3270 3.2; 3597 2.1; 3957 1.5; 4353 1.5; 4788 0.6; 5267 3.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One S 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One S 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.47 | -3.6 dB |
| Peaking | 118 Hz  | 1.33 | -4.2 dB |
| Peaking | 186 Hz  | 2.69 | -3.2 dB |
| Peaking | 2714 Hz | 1.99 | 4.3 dB  |
| Peaking | 5990 Hz | 4.28 | 6.5 dB  |
| Peaking | 239 Hz  | 3.34 | -1.1 dB |
| Peaking | 331 Hz  | 2.18 | 2.3 dB  |
| Peaking | 511 Hz  | 2.01 | -1.7 dB |
| Peaking | 6684 Hz | 8.57 | 1.7 dB  |
| Peaking | 8104 Hz | 1.44 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20S%202014/Focal%20Spirit%20One%20S%202014.png)