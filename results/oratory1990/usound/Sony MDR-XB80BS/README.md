# Sony MDR-XB80BS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -1.7; 23 -1.7; 25 -1.8; 28 -1.8; 31 -1.9; 34 -2.0; 37 -2.1; 41 -2.2; 45 -2.3; 49 -2.5; 54 -2.8; 60 -3.1; 66 -3.4; 72 -3.7; 79 -4.0; 87 -4.4; 96 -5.0; 106 -5.4; 116 -5.4; 128 -5.4; 141 -5.3; 155 -4.9; 170 -4.4; 187 -3.7; 206 -2.9; 227 -2.0; 249 -1.3; 274 -0.7; 302 -0.3; 332 -0.0; 365 0.1; 402 0.1; 442 0.0; 486 -0.1; 535 -0.2; 588 -0.2; 647 -0.2; 712 -0.1; 783 -0.0; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.0; 1387 0.4; 1526 0.9; 1678 1.5; 1846 1.9; 2031 1.7; 2234 1.1; 2457 0.3; 2703 0.1; 2973 1.2; 3270 3.0; 3597 4.5; 3957 5.5; 4353 5.8; 4788 5.2; 5267 2.7; 5793 -1.2; 6373 0.1; 7010 2.3; 7711 0.3; 8482 -0.9; 9330 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB80BS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.29 | -1.6 dB |
| Peaking | 102 Hz  | 1.07 | -1.7 dB |
| Peaking | 150 Hz  | 0.87 | -3.9 dB |
| Peaking | 294 Hz  | 1.16 | 1.6 dB  |
| Peaking | 4151 Hz | 2.51 | 6.4 dB  |
| Peaking | 1877 Hz | 3.3  | 1.8 dB  |
| Peaking | 2653 Hz | 5.8  | -1.4 dB |
| Peaking | 5627 Hz | 7.32 | -2.0 dB |
| Peaking | 5951 Hz | 2.92 | 2.8 dB  |
| Peaking | 5973 Hz | 8.09 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)