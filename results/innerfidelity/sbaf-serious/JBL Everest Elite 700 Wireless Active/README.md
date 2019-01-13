# JBL Everest Elite 700 Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.7; 25 -1.5; 28 -2.3; 31 -2.5; 34 -2.5; 37 -2.3; 41 -2.0; 45 -1.6; 49 -1.2; 54 -0.7; 60 -0.3; 66 0.1; 72 0.4; 79 0.7; 87 0.8; 96 0.7; 106 0.7; 116 0.7; 128 0.7; 141 0.5; 155 0.5; 170 0.4; 187 0.3; 206 0.0; 227 0.3; 249 0.4; 274 0.7; 302 0.8; 332 1.0; 365 1.1; 402 1.3; 442 1.4; 486 0.9; 535 0.7; 588 0.9; 647 0.8; 712 0.8; 783 0.9; 861 0.7; 947 0.3; 1042 -0.1; 1146 0.0; 1261 -1.0; 1387 -1.1; 1526 -1.7; 1678 -2.5; 1846 -3.1; 2031 -4.0; 2234 -4.9; 2457 -4.5; 2703 -3.1; 2973 -1.0; 3270 0.8; 3597 0.7; 3957 1.4; 4353 3.2; 4788 5.9; 5267 6.0; 5793 5.9; 6373 4.6; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -3.2; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.44 | -3.3 dB |
| Peaking | 259 Hz  | 0.07 | 0.8 dB  |
| Peaking | 2235 Hz | 1.57 | -6.1 dB |
| Peaking | 5480 Hz | 1.6  | 6.9 dB  |
| Peaking | 8959 Hz | 3.2  | -4.9 dB |
| Peaking | 16 Hz   | 2.41 | 1.9 dB  |
| Peaking | 46 Hz   | 2.65 | -0.5 dB |
| Peaking | 211 Hz  | 2.41 | -0.8 dB |
| Peaking | 415 Hz  | 1.68 | 0.5 dB  |
| Peaking | 4698 Hz | 7.03 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wireless%20Active/JBL%20Everest%20Elite%20700%20Wireless%20Active.png)