# JBL J88i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.6; 28 2.2; 31 1.9; 34 1.6; 37 1.4; 41 1.2; 45 1.0; 49 0.8; 54 0.6; 60 0.3; 66 0.0; 72 -0.3; 79 -0.6; 87 -1.0; 96 -1.5; 106 -1.7; 116 -2.0; 128 -2.5; 141 -2.9; 155 -3.2; 170 -2.8; 187 -3.2; 206 -3.4; 227 -3.5; 249 -3.6; 274 -3.3; 302 -2.8; 332 -1.8; 365 -0.5; 402 1.8; 442 4.9; 486 5.6; 535 6.0; 588 6.0; 647 4.9; 712 2.4; 783 1.3; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.8; 1387 -1.1; 1526 -0.8; 1678 0.6; 1846 3.1; 2031 5.6; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J88i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J88i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 406 Hz  | 0.39 | -7.6 dB |
| Peaking | 520 Hz  | 1.33 | 13.5 dB |
| Peaking | 1444 Hz | 2.68 | -4.0 dB |
| Peaking | 2964 Hz | 0.6  | 7.6 dB  |
| Peaking | 17 Hz   | 0.8  | 3.5 dB  |
| Peaking | 56 Hz   | 0.95 | 0.7 dB  |
| Peaking | 3267 Hz | 4.23 | -1.1 dB |
| Peaking | 6195 Hz | 2.13 | 5.0 dB  |
| Peaking | 7611 Hz | 1.47 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J88i/JBL%20J88i.png)