# Sony MDR-V500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.7; 116 4.8; 128 3.9; 141 3.2; 155 3.7; 170 3.2; 187 2.9; 206 2.8; 227 3.7; 249 3.4; 274 3.1; 302 2.1; 332 2.1; 365 2.0; 402 1.9; 442 1.7; 486 1.4; 535 1.1; 588 1.2; 647 1.4; 712 0.7; 783 0.7; 861 1.1; 947 0.2; 1042 -0.3; 1146 0.1; 1261 -0.9; 1387 -2.2; 1526 -2.7; 1678 -2.7; 1846 -2.9; 2031 -2.9; 2234 -3.0; 2457 -3.1; 2703 -3.0; 2973 -4.2; 3270 -4.3; 3597 -3.7; 3957 -3.4; 4353 -2.6; 4788 -1.2; 5267 0.7; 5793 1.0; 6373 -1.2; 7010 0.8; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -2.1; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.27 | 5.5 dB  |
| Peaking | 207 Hz   | 0.2  | 1.8 dB  |
| Peaking | 3613 Hz  | 0.58 | -6.4 dB |
| Peaking | 5589 Hz  | 0.94 | 4.9 dB  |
| Peaking | 10251 Hz | 8.57 | -2.1 dB |
| Peaking | 100 Hz   | 2.06 | 2.3 dB  |
| Peaking | 116 Hz   | 0.99 | -1.7 dB |
| Peaking | 241 Hz   | 4.87 | 1.2 dB  |
| Peaking | 1506 Hz  | 6.11 | -1.1 dB |
| Peaking | 2546 Hz  | 5.84 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V500/Sony%20MDR-V500.png)