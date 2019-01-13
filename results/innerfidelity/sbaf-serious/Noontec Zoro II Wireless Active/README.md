# Noontec Zoro II Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -0.7; 28 -1.3; 31 -1.7; 34 -2.0; 37 -2.3; 41 -2.6; 45 -2.8; 49 -2.9; 54 -3.2; 60 -3.4; 66 -3.4; 72 -3.7; 79 -4.1; 87 -4.8; 96 -5.2; 106 -5.6; 116 -5.9; 128 -6.1; 141 -6.5; 155 -6.7; 170 -6.4; 187 -6.7; 206 -6.5; 227 -6.3; 249 -6.0; 274 -5.4; 302 -4.8; 332 -4.6; 365 -4.1; 402 -4.0; 442 -3.7; 486 -3.4; 535 -2.8; 588 -1.9; 647 -1.4; 712 -0.9; 783 -0.2; 861 -0.1; 947 0.0; 1042 -0.0; 1146 0.0; 1261 -0.6; 1387 -1.2; 1526 -1.7; 1678 -1.9; 1846 -1.6; 2031 -0.9; 2234 0.1; 2457 1.0; 2703 1.6; 2973 2.0; 3270 1.8; 3597 2.4; 3957 5.0; 4353 4.4; 4788 3.0; 5267 1.4; 5793 2.3; 6373 0.2; 7010 0.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 0.41 | -2.7 dB |
| Peaking | 207 Hz  | 0.59 | -4.8 dB |
| Peaking | 1704 Hz | 4.19 | -2.2 dB |
| Peaking | 4108 Hz | 2.18 | 4.7 dB  |
| Peaking | 71 Hz   | 4.68 | 0.4 dB  |
| Peaking | 481 Hz  | 3.24 | -1.0 dB |
| Peaking | 874 Hz  | 1.87 | 1.1 dB  |
| Peaking | 2604 Hz | 3.4  | 1.9 dB  |
| Peaking | 2636 Hz | 1.15 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Active/Noontec%20Zoro%20II%20Wireless%20Active.png)