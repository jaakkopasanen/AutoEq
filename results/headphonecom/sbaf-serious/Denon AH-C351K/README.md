# Denon AH-C351K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.8; 28 -1.9; 31 -2.0; 34 -2.0; 37 -2.1; 41 -2.2; 45 -2.3; 49 -2.5; 54 -2.7; 60 -3.0; 66 -3.3; 72 -3.5; 79 -3.9; 87 -4.2; 96 -4.5; 106 -4.7; 116 -5.0; 128 -5.3; 141 -5.6; 155 -5.7; 170 -5.7; 187 -5.9; 206 -5.7; 227 -5.7; 249 -5.5; 274 -5.3; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.5; 442 -4.1; 486 -3.6; 535 -3.1; 588 -2.5; 647 -2.0; 712 -1.4; 783 -0.9; 861 -0.5; 947 -0.3; 1042 0.1; 1146 0.5; 1261 0.8; 1387 1.0; 1526 0.9; 1678 0.8; 1846 1.7; 2031 3.0; 2234 4.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 3.5; 5267 1.0; 5793 -4.3; 6373 -2.8; 7010 1.0; 7711 0.3; 8482 -1.9; 9330 -4.3; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.2; 16529 -1.0; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C351K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C351K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 59 Hz    | 0.15 | -1.5 dB |
| Peaking | 219 Hz   | 0.44 | -4.8 dB |
| Peaking | 3417 Hz  | 0.85 | 6.9 dB  |
| Peaking | 5956 Hz  | 5.63 | -8.6 dB |
| Peaking | 9158 Hz  | 5.5  | -5.6 dB |
| Peaking | 1784 Hz  | 2.33 | -3.6 dB |
| Peaking | 2096 Hz  | 1.05 | 2.7 dB  |
| Peaking | 3231 Hz  | 2.91 | -1.7 dB |
| Peaking | 15601 Hz | 4.15 | -3.8 dB |
| Peaking | 15708 Hz | 1.3  | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C351K/Denon%20AH-C351K.png)