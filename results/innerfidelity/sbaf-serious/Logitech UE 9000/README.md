# Logitech UE 9000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.5; 25 -0.8; 28 -1.1; 31 -1.3; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.8; 49 -1.8; 54 -1.9; 60 -1.9; 66 -2.0; 72 -2.0; 79 -2.1; 87 -2.0; 96 -2.1; 106 -2.1; 116 -2.6; 128 -3.6; 141 -3.4; 155 -2.6; 170 -1.7; 187 -1.7; 206 -2.2; 227 -1.6; 249 -1.0; 274 -0.4; 302 -0.1; 332 0.3; 365 0.7; 402 1.0; 442 1.3; 486 1.2; 535 1.3; 588 1.6; 647 1.4; 712 0.9; 783 0.9; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 0.0; 1387 0.1; 1526 0.0; 1678 0.2; 1846 1.1; 2031 1.9; 2234 3.2; 2457 4.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 4.8; 4353 4.2; 4788 3.5; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 9000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 9000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.76 | -1.9 dB |
| Peaking | 138 Hz  | 1.82 | -3.0 dB |
| Peaking | 3112 Hz | 1.63 | 6.5 dB  |
| Peaking | 5819 Hz | 3.35 | 5.5 dB  |
| Peaking | 217 Hz  | 4.8  | -1.5 dB |
| Peaking | 566 Hz  | 0.98 | 1.7 dB  |
| Peaking | 1324 Hz | 1.09 | -1.2 dB |
| Peaking | 2518 Hz | 6.93 | 1.5 dB  |
| Peaking | 8281 Hz | 4.41 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%209000/Logitech%20UE%209000.png)