# Audio-Technica ATH-ANC9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -7.1; 23 -7.6; 25 -7.9; 28 -8.3; 31 -8.5; 34 -8.5; 37 -8.4; 41 -8.1; 45 -7.8; 49 -7.5; 54 -7.0; 60 -6.6; 66 -6.4; 72 -6.2; 79 -6.2; 87 -6.4; 96 -6.8; 106 -7.4; 116 -7.8; 128 -8.1; 141 -8.1; 155 -7.8; 170 -7.2; 187 -6.5; 206 -5.7; 227 -4.9; 249 -4.1; 274 -3.4; 302 -2.9; 332 -2.4; 365 -1.9; 402 -1.6; 442 -1.4; 486 -1.4; 535 -1.4; 588 -1.2; 647 -0.0; 712 1.4; 783 2.3; 861 2.7; 947 1.4; 1042 -1.0; 1146 -3.1; 1261 -4.8; 1387 -5.6; 1526 -6.0; 1678 -5.6; 1846 -5.1; 2031 -4.5; 2234 -4.3; 2457 -4.0; 2703 -4.1; 2973 -3.6; 3270 -2.8; 3597 -2.7; 3957 -5.2; 4353 -5.8; 4788 -7.3; 5267 -6.7; 5793 -5.2; 6373 -2.6; 7010 -2.3; 7711 -3.5; 8482 -2.9; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 -2.3; 13660 -5.1; 15026 -3.7; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.52 | -8.1 dB |
| Peaking | 147 Hz   | 0.95 | -6.9 dB |
| Peaking | 1662 Hz  | 1.88 | -5.9 dB |
| Peaking | 4869 Hz  | 1.54 | -6.7 dB |
| Peaking | 13990 Hz | 3.63 | -5.6 dB |
| Peaking | 627 Hz   | 1.21 | -1.6 dB |
| Peaking | 830 Hz   | 2.12 | 5.3 dB  |
| Peaking | 1222 Hz  | 3.49 | -2.7 dB |
| Peaking | 8191 Hz  | 4.8  | -4.1 dB |
| Peaking | 8935 Hz  | 1.87 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC9/Audio-Technica%20ATH-ANC9.png)