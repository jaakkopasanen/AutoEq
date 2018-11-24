# Sony MDR-ZX550BN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.9; 141 5.6; 155 5.8; 170 6.0; 187 6.0; 206 5.7; 227 5.6; 249 6.0; 274 6.0; 302 6.0; 332 5.6; 365 4.6; 402 3.8; 442 3.2; 486 2.7; 535 2.2; 588 1.8; 647 1.6; 712 1.2; 783 0.7; 861 0.2; 947 -0.0; 1042 0.1; 1146 0.5; 1261 0.6; 1387 0.1; 1526 0.1; 1678 1.1; 1846 2.5; 2031 4.1; 2234 5.4; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.7; 8482 -6.4; 9330 -4.7; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.1; 18182 -2.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX550BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX550BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.16 | 6.5 dB   |
| Peaking | 2664 Hz  | 2.12 | 4.6 dB   |
| Peaking | 5563 Hz  | 0.96 | 7.0 dB   |
| Peaking | 8587 Hz  | 3.4  | -10.6 dB |
| Peaking | 17564 Hz | 3.61 | -4.5 dB  |
| Peaking | 301 Hz   | 2.71 | 1.9 dB   |
| Peaking | 899 Hz   | 1.5  | -1.4 dB  |
| Peaking | 1503 Hz  | 4.97 | -1.4 dB  |
| Peaking | 2112 Hz  | 5.75 | 1.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-ZX550BN/Sony%20MDR-ZX550BN.png)