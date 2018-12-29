# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 0.0; 23 0.9; 25 -0.2; 28 -1.5; 31 -2.4; 34 -3.0; 37 -3.4; 41 -3.6; 45 -3.7; 49 -3.7; 54 -3.6; 60 -3.5; 66 -3.4; 72 -3.3; 79 -3.0; 87 -2.9; 96 -3.3; 106 -3.9; 116 -4.1; 128 -3.6; 141 -4.5; 155 -5.6; 170 -4.6; 187 -4.7; 206 -4.4; 227 -3.9; 249 -3.4; 274 -2.8; 302 -2.0; 332 -1.4; 365 -0.9; 402 -0.3; 442 0.3; 486 0.2; 535 0.3; 588 0.6; 647 0.4; 712 -0.2; 783 -0.8; 861 -1.2; 947 -0.6; 1042 0.6; 1146 3.0; 1261 4.3; 1387 4.4; 1526 3.0; 1678 0.8; 1846 -1.3; 2031 -2.9; 2234 -4.1; 2457 -4.7; 2703 -3.5; 2973 -1.9; 3270 0.6; 3597 2.9; 3957 2.2; 4353 0.2; 4788 0.2; 5267 2.9; 5793 3.1; 6373 1.2; 7010 1.1; 7711 0.3; 8482 -0.7; 9330 -1.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.48 | 5.7 dB  |
| Peaking | 39 Hz   | 0.53 | -4.1 dB |
| Peaking | 173 Hz  | 1.15 | -4.5 dB |
| Peaking | 1341 Hz | 3.46 | 5.4 dB  |
| Peaking | 2333 Hz | 3.66 | -5.5 dB |
| Peaking | 490 Hz  | 2.2  | 1.5 dB  |
| Peaking | 1138 Hz | 0.22 | -0.5 dB |
| Peaking | 3678 Hz | 6.51 | 4.0 dB  |
| Peaking | 5634 Hz | 4.57 | 3.8 dB  |
| Peaking | 9072 Hz | 7.69 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z7/Sony%20MDR-Z7.png)