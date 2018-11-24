# Noontec Zoro II HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.4; 34 -1.4; 37 -1.4; 41 -1.5; 45 -1.4; 49 -1.4; 54 -1.5; 60 -1.8; 66 -1.9; 72 -2.0; 79 -2.2; 87 -2.2; 96 -2.7; 106 -3.0; 116 -2.8; 128 -2.6; 141 -3.3; 155 -3.9; 170 -3.5; 187 -3.9; 206 -3.8; 227 -3.5; 249 -3.1; 274 -2.5; 302 -2.0; 332 -1.9; 365 -1.7; 402 -1.5; 442 -1.3; 486 -1.3; 535 -0.6; 588 -0.2; 647 0.1; 712 0.1; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.5; 1387 -1.1; 1526 -1.7; 1678 -1.9; 1846 -1.6; 2031 -0.7; 2234 0.1; 2457 1.4; 2703 1.9; 2973 2.8; 3270 3.4; 3597 5.2; 3957 6.0; 4353 5.8; 4788 3.6; 5267 3.2; 5793 4.1; 6373 2.8; 7010 2.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.36 | -1.5 dB |
| Peaking | 193 Hz  | 0.94 | -3.1 dB |
| Peaking | 1696 Hz | 3.04 | -2.5 dB |
| Peaking | 3928 Hz | 1.99 | 6.1 dB  |
| Peaking | 5963 Hz | 4.72 | 2.5 dB  |
| Peaking | 474 Hz  | 3.19 | -0.6 dB |
| Peaking | 604 Hz  | 3.16 | 0.5 dB  |
| Peaking | 807 Hz  | 3.78 | 0.7 dB  |
| Peaking | 8143 Hz | 8.19 | -0.6 dB |
| Peaking | 9874 Hz | 2.96 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20HD/Noontec%20Zoro%20II%20HD.png)