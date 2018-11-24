# Sony MDR-ZX550BN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.9; 128 5.4; 141 5.1; 155 5.2; 170 5.5; 187 5.5; 206 5.2; 227 5.2; 249 5.9; 274 6.0; 302 5.8; 332 4.7; 365 3.5; 402 2.7; 442 2.1; 486 1.4; 535 1.0; 588 0.7; 647 0.5; 712 0.4; 783 0.2; 861 0.0; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.3; 1387 0.1; 1526 0.5; 1678 1.5; 1846 2.5; 2031 3.7; 2234 4.9; 2457 5.6; 2703 5.5; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -2.8; 8482 -6.7; 9330 -6.2; 10263 -2.6; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -5.3; 18182 -6.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX550BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX550BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.24 | 6.4 dB   |
| Peaking | 273 Hz   | 1.89 | 3.8 dB   |
| Peaking | 5280 Hz  | 0.57 | 8.1 dB   |
| Peaking | 8719 Hz  | 2.5  | -13.0 dB |
| Peaking | 17461 Hz | 2.75 | -8.6 dB  |
| Peaking | 1597 Hz  | 0.8  | -2.5 dB  |
| Peaking | 2331 Hz  | 1.52 | 3.6 dB   |
| Peaking | 5212 Hz  | 1.23 | -1.1 dB  |
| Peaking | 6333 Hz  | 4.78 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-ZX550BN/Sony%20MDR-ZX550BN.png)