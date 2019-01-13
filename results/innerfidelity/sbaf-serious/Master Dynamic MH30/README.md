# Master Dynamic MH30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.1; 23 -4.2; 25 -4.3; 28 -4.3; 31 -4.4; 34 -4.4; 37 -4.3; 41 -4.3; 45 -4.2; 49 -4.3; 54 -4.3; 60 -4.4; 66 -4.4; 72 -4.4; 79 -4.5; 87 -4.5; 96 -4.5; 106 -4.7; 116 -4.7; 128 -4.8; 141 -4.7; 155 -4.8; 170 -4.3; 187 -4.4; 206 -4.0; 227 -3.4; 249 -2.7; 274 -1.9; 302 -1.6; 332 -1.5; 365 -1.7; 402 -1.8; 442 -2.0; 486 -2.2; 535 -2.2; 588 -1.9; 647 -1.9; 712 -1.9; 783 -1.4; 861 -1.1; 947 -0.4; 1042 0.4; 1146 1.3; 1261 2.0; 1387 2.4; 1526 2.6; 1678 2.7; 1846 2.9; 2031 3.0; 2234 2.6; 2457 2.6; 2703 3.0; 2973 3.2; 3270 3.6; 3597 5.1; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic MH30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.25 | -4.3 dB |
| Peaking | 156 Hz  | 1.03 | -2.8 dB |
| Peaking | 733 Hz  | 0.94 | -3.2 dB |
| Peaking | 1448 Hz | 0.74 | 3.4 dB  |
| Peaking | 4772 Hz | 1.45 | 6.4 dB  |
| Peaking | 3825 Hz | 5.47 | 1.6 dB  |
| Peaking | 4677 Hz | 2.3  | -1.1 dB |
| Peaking | 6305 Hz | 3.26 | 4.3 dB  |
| Peaking | 7450 Hz | 1.7  | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH30/Master%20Dynamic%20MH30.png)