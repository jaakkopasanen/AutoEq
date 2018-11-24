# Denon AH-C560R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 21 -4.8; 23 -5.3; 25 -5.6; 28 -6.1; 31 -6.4; 34 -6.8; 37 -7.0; 41 -7.3; 45 -7.6; 49 -7.9; 54 -8.2; 60 -8.7; 66 -9.0; 72 -9.3; 79 -9.5; 87 -9.6; 96 -9.9; 106 -10.0; 116 -10.1; 128 -10.2; 141 -10.2; 155 -10.2; 170 -10.0; 187 -9.9; 206 -9.5; 227 -9.1; 249 -8.7; 274 -8.2; 302 -7.6; 332 -6.9; 365 -6.2; 402 -5.5; 442 -4.8; 486 -4.2; 535 -3.5; 588 -2.8; 647 -2.7; 712 -1.8; 783 -1.3; 861 -0.9; 947 -0.3; 1042 -0.0; 1146 -0.4; 1261 -0.8; 1387 -1.2; 1526 -1.8; 1678 -2.1; 1846 -2.1; 2031 -2.0; 2234 -1.9; 2457 -2.0; 2703 -2.3; 2973 -2.5; 3270 -2.1; 3597 -1.5; 3957 -2.2; 4353 -4.4; 4788 -6.2; 5267 -7.6; 5793 -8.8; 6373 -6.3; 7010 -4.3; 7711 -4.6; 8482 -7.4; 9330 -8.6; 10263 -3.1; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -2.8; 16529 -0.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.43 | -4.8 dB |
| Peaking | 100 Hz   | 0.58 | -5.3 dB |
| Peaking | 235 Hz   | 0.62 | -6.3 dB |
| Peaking | 5542 Hz  | 1.74 | -7.9 dB |
| Peaking | 9037 Hz  | 4.97 | -8.0 dB |
| Peaking | 1052 Hz  | 1.48 | 2.7 dB  |
| Peaking | 1546 Hz  | 0.69 | -2.2 dB |
| Peaking | 3797 Hz  | 4.9  | 1.9 dB  |
| Peaking | 11530 Hz | 4.21 | 1.8 dB  |
| Peaking | 15192 Hz | 5.86 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)