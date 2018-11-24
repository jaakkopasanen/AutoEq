# Sony MDR-AS50G

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.4; 25 -1.8; 28 -2.3; 31 -2.7; 34 -3.0; 37 -3.3; 41 -3.6; 45 -3.9; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.0; 96 -6.1; 106 -6.3; 116 -6.3; 128 -6.4; 141 -6.4; 155 -6.3; 170 -6.1; 187 -5.9; 206 -5.6; 227 -5.2; 249 -4.9; 274 -4.6; 302 -4.1; 332 -3.6; 365 -3.0; 402 -2.6; 442 -2.2; 486 -1.8; 535 -1.3; 588 -0.8; 647 -0.4; 712 -0.2; 783 -0.0; 861 0.1; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -3.2; 1678 -4.0; 1846 -4.3; 2031 -4.1; 2234 -3.5; 2457 -2.1; 2703 0.3; 2973 4.2; 3270 6.0; 3597 6.0; 3957 5.9; 4353 1.7; 4788 -2.3; 5267 -3.5; 5793 -1.5; 6373 -0.4; 7010 -2.3; 7711 -6.3; 8482 -5.7; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -3.3; 15026 -4.1; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-AS50G GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-AS50G ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 88 Hz    | 0.47 | -5.4 dB |
| Peaking | 216 Hz   | 0.91 | -2.9 dB |
| Peaking | 1976 Hz  | 1.92 | -5.2 dB |
| Peaking | 3399 Hz  | 3.16 | 8.2 dB  |
| Peaking | 7949 Hz  | 3.95 | -7.2 dB |
| Peaking | 867 Hz   | 2.48 | 1.1 dB  |
| Peaking | 4032 Hz  | 9    | 3.2 dB  |
| Peaking | 5058 Hz  | 5.08 | -4.5 dB |
| Peaking | 12913 Hz | 0.82 | 1.6 dB  |
| Peaking | 14467 Hz | 3.79 | -7.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-AS50G/Sony%20MDR-AS50G.png)