# Logitech UE 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.1; 25 1.1; 28 1.0; 31 0.9; 34 0.7; 37 0.6; 41 0.5; 45 0.4; 49 0.2; 54 -0.0; 60 -0.5; 66 -0.8; 72 -1.1; 79 -1.5; 87 -1.9; 96 -2.4; 106 -2.7; 116 -2.9; 128 -3.2; 141 -3.6; 155 -3.8; 170 -4.0; 187 -4.2; 206 -4.3; 227 -4.4; 249 -4.5; 274 -4.5; 302 -4.6; 332 -4.7; 365 -4.8; 402 -4.9; 442 -4.9; 486 -5.1; 535 -5.1; 588 -4.7; 647 -4.0; 712 -3.0; 783 -1.6; 861 -0.7; 947 -0.1; 1042 0.0; 1146 0.0; 1261 -0.3; 1387 -0.8; 1526 -1.4; 1678 -2.0; 1846 -2.3; 2031 -2.4; 2234 -2.3; 2457 -1.2; 2703 1.4; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.3; 4788 5.5; 5267 5.6; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -1.5; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.87 | 1.4 dB  |
| Peaking | 289 Hz  | 0.45 | -5.1 dB |
| Peaking | 2253 Hz | 2.21 | -5.6 dB |
| Peaking | 3351 Hz | 1.39 | 7.6 dB  |
| Peaking | 5778 Hz | 3.27 | 4.5 dB  |
| Peaking | 284 Hz  | 2.16 | 0.8 dB  |
| Peaking | 613 Hz  | 1.46 | -2.9 dB |
| Peaking | 889 Hz  | 1.19 | 2.8 dB  |
| Peaking | 1635 Hz | 3.43 | -1.4 dB |
| Peaking | 9199 Hz | 4.01 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%20900/Logitech%20UE%20900.png)