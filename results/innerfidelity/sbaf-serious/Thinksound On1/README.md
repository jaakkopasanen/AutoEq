# Thinksound On1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.1; 23 -0.6; 25 -1.1; 28 -1.7; 31 -2.2; 34 -2.6; 37 -2.9; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.5; 60 -3.4; 66 -3.8; 72 -4.3; 79 -4.4; 87 -4.5; 96 -4.2; 106 -3.6; 116 -2.9; 128 -2.4; 141 -1.7; 155 -1.3; 170 0.1; 187 0.3; 206 1.4; 227 2.6; 249 3.4; 274 3.5; 302 3.2; 332 2.5; 365 2.1; 402 1.9; 442 1.6; 486 1.1; 535 0.9; 588 1.0; 647 0.7; 712 0.5; 783 0.4; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.2; 1261 0.3; 1387 0.2; 1526 0.2; 1678 0.3; 1846 1.3; 2031 3.3; 2234 3.5; 2457 4.3; 2703 6.0; 2973 5.6; 3270 4.1; 3597 3.8; 3957 4.5; 4353 4.0; 4788 4.9; 5267 6.0; 5793 3.5; 6373 2.6; 7010 0.4; 7711 -0.2; 8482 -1.6; 9330 -0.3; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -1.0; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound On1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound On1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 1.58 | -1.8 dB |
| Peaking | 87 Hz   | 0.82 | -4.5 dB |
| Peaking | 270 Hz  | 1.31 | 4.2 dB  |
| Peaking | 2791 Hz | 1.99 | 5.6 dB  |
| Peaking | 5091 Hz | 3.11 | 5.4 dB  |
| Peaking | 1926 Hz | 1.64 | -1.5 dB |
| Peaking | 2053 Hz | 5.19 | 2.6 dB  |
| Peaking | 4608 Hz | 2.42 | 2.1 dB  |
| Peaking | 4702 Hz | 5.42 | -2.5 dB |
| Peaking | 8443 Hz | 4.22 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20On1/Thinksound%20On1.png)