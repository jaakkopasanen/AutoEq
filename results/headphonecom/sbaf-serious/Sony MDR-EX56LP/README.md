# Sony MDR-EX56LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.3; 28 -8.7; 31 -9.0; 34 -9.3; 37 -9.5; 41 -9.8; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.7; 66 -10.8; 72 -11.0; 79 -11.1; 87 -11.2; 96 -11.2; 106 -11.1; 116 -11.0; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.2; 187 -9.8; 206 -9.4; 227 -8.9; 249 -8.4; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.1; 402 -5.6; 442 -5.2; 486 -5.0; 535 -4.6; 588 -4.2; 647 -4.0; 712 -4.2; 783 -4.5; 861 -4.6; 947 -1.0; 1042 -0.5; 1146 -2.1; 1261 -3.4; 1387 -4.7; 1526 -6.1; 1678 -7.1; 1846 -8.0; 2031 -8.5; 2234 -8.3; 2457 -7.2; 2703 -5.5; 2973 -3.6; 3270 -1.9; 3597 -0.6; 3957 2.2; 4353 5.7; 4788 6.0; 5267 6.0; 5793 5.4; 6373 1.2; 7010 0.3; 7711 0.3; 8482 -0.0; 9330 -2.3; 10263 -3.8; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 -1.7; 16529 -2.9; 18182 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX56LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX56LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.31 | -6.5 dB |
| Peaking | 153 Hz   | 0.34 | -8.4 dB |
| Peaking | 2119 Hz  | 1.42 | -8.9 dB |
| Peaking | 4821 Hz  | 2.53 | 8.4 dB  |
| Peaking | 866 Hz   | 3.58 | -3.7 dB |
| Peaking | 981 Hz   | 4.04 | 5.0 dB  |
| Peaking | 1521 Hz  | 5.08 | -1.1 dB |
| Peaking | 9824 Hz  | 5.75 | -4.3 dB |
| Peaking | 16164 Hz | 4.28 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX56LP/Sony%20MDR-EX56LP.png)