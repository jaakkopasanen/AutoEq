# Fischer Audio FA-011 LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.9dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.3; 28 3.1; 31 2.0; 34 1.1; 37 0.3; 41 -0.4; 45 -1.0; 49 -1.4; 54 -1.8; 60 -2.0; 66 -2.2; 72 -2.2; 79 -2.4; 87 -2.5; 96 -2.6; 106 -2.6; 116 -2.5; 128 -2.5; 141 -2.4; 155 -2.3; 170 -2.4; 187 -1.8; 206 -2.1; 227 -2.0; 249 -2.0; 274 -1.7; 302 -1.9; 332 -1.9; 365 -1.9; 402 -1.9; 442 -1.8; 486 -1.8; 535 -1.9; 588 -1.5; 647 -0.8; 712 -0.2; 783 -0.1; 861 -0.5; 947 -0.3; 1042 0.3; 1146 1.0; 1261 1.9; 1387 2.3; 1526 2.4; 1678 2.7; 1846 3.5; 2031 4.4; 2234 5.2; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 5.2; 4788 6.0; 5267 5.2; 5793 5.2; 6373 4.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-011 LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-011 LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.01 | 7.4 dB  |
| Peaking | 47 Hz   | 0.97 | -1.5 dB |
| Peaking | 109 Hz  | 0.55 | -2.3 dB |
| Peaking | 473 Hz  | 0.79 | -1.7 dB |
| Peaking | 3299 Hz | 0.71 | 6.6 dB  |
| Peaking | 14 Hz   | 0.83 | 0.4 dB  |
| Peaking | 2342 Hz | 3.27 | 0.6 dB  |
| Peaking | 3392 Hz | 2.07 | -0.8 dB |
| Peaking | 6303 Hz | 1.9  | 4.5 dB  |
| Peaking | 7527 Hz | 1.45 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-011%20LE/Fischer%20Audio%20FA-011%20LE.png)