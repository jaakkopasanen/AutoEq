# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.1; 28 1.7; 31 1.4; 34 1.2; 37 1.1; 41 1.1; 45 1.1; 49 1.2; 54 1.1; 60 0.6; 66 0.4; 72 0.4; 79 0.4; 87 0.1; 96 -0.1; 106 -0.2; 116 -0.2; 128 -0.4; 141 -0.6; 155 -0.6; 170 -0.7; 187 -0.9; 206 -0.8; 227 -1.0; 249 -1.1; 274 -1.2; 302 -1.0; 332 -0.9; 365 -1.1; 402 -0.7; 442 -0.9; 486 -1.1; 535 -0.8; 588 -1.0; 647 -0.7; 712 -0.1; 783 0.6; 861 0.1; 947 0.1; 1042 -0.4; 1146 0.1; 1261 0.4; 1387 1.1; 1526 0.6; 1678 1.1; 1846 2.4; 2031 2.7; 2234 0.8; 2457 2.5; 2703 2.4; 2973 0.9; 3270 0.4; 3597 0.6; 3957 0.1; 4353 -1.6; 4788 -1.3; 5267 2.0; 5793 2.2; 6373 0.4; 7010 -0.1; 7711 -0.5; 8482 -3.7; 9330 -6.0; 10263 -1.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.8; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.93 | 2.6 dB  |
| Peaking | 2237 Hz  | 1.61 | 2.3 dB  |
| Peaking | 4628 Hz  | 4.28 | -3.2 dB |
| Peaking | 5414 Hz  | 4.17 | 3.6 dB  |
| Peaking | 9092 Hz  | 5.24 | -6.7 dB |
| Peaking | 53 Hz    | 1.79 | 0.6 dB  |
| Peaking | 322 Hz   | 0.48 | -1.1 dB |
| Peaking | 771 Hz   | 8.04 | 1.2 dB  |
| Peaking | 1876 Hz  | 9.56 | 1.0 dB  |
| Peaking | 19651 Hz | 2.29 | -5.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)