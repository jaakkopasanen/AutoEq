# JBL Everest Elite 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.0; 31 -1.1; 34 -1.2; 37 -1.1; 41 -1.0; 45 -1.0; 49 -1.0; 54 -0.9; 60 -0.7; 66 -0.5; 72 -0.1; 79 0.2; 87 0.3; 96 0.5; 106 0.5; 116 0.5; 128 0.5; 141 0.6; 155 0.6; 170 0.6; 187 0.5; 206 0.3; 227 0.3; 249 0.4; 274 0.6; 302 0.9; 332 1.1; 365 1.5; 402 1.3; 442 1.0; 486 0.8; 535 0.6; 588 0.5; 647 0.8; 712 0.9; 783 0.8; 861 0.4; 947 0.0; 1042 0.1; 1146 0.5; 1261 -0.8; 1387 -2.6; 1526 -2.7; 1678 -2.3; 1846 -2.5; 2031 -2.5; 2234 -2.4; 2457 -2.0; 2703 -1.4; 2973 -0.7; 3270 0.6; 3597 2.2; 3957 2.0; 4353 2.3; 4788 5.7; 5267 6.0; 5793 4.7; 6373 2.9; 7010 2.4; 7711 0.3; 8482 -1.3; 9330 -5.5; 10263 -6.1; 11289 -4.3; 12418 -0.9; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 1.31 | -1.3 dB |
| Peaking | 1922 Hz  | 0.96 | -4.7 dB |
| Peaking | 2201 Hz  | 0.11 | 1.7 dB  |
| Peaking | 5270 Hz  | 2.12 | 5.6 dB  |
| Peaking | 10056 Hz | 2.49 | -8.3 dB |
| Peaking | 376 Hz   | 1.45 | -1.1 dB |
| Peaking | 378 Hz   | 2.97 | 1.7 dB  |
| Peaking | 1167 Hz  | 5.32 | 1.6 dB  |
| Peaking | 1421 Hz  | 3.27 | -1.8 dB |
| Peaking | 1684 Hz  | 3.79 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)