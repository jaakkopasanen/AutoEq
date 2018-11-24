# HiFiMAN HE-300 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.4; 28 4.3; 31 3.1; 34 2.0; 37 1.0; 41 -0.1; 45 -1.0; 49 -1.6; 54 -2.1; 60 -2.6; 66 -2.9; 72 -3.7; 79 -4.4; 87 -4.6; 96 -5.1; 106 -5.3; 116 -5.2; 128 -5.1; 141 -4.7; 155 -4.3; 170 -3.7; 187 -3.4; 206 -2.9; 227 -2.7; 249 -3.4; 274 -2.7; 302 -2.0; 332 -1.4; 365 -0.9; 402 -0.5; 442 -0.0; 486 0.3; 535 0.9; 588 1.6; 647 1.7; 712 2.1; 783 1.5; 861 0.7; 947 0.2; 1042 -0.2; 1146 -1.0; 1261 -1.6; 1387 -2.6; 1526 -3.5; 1678 -3.9; 1846 -4.0; 2031 -4.8; 2234 -4.3; 2457 -3.7; 2703 -3.8; 2973 -5.1; 3270 -5.9; 3597 -4.6; 3957 -3.9; 4353 -5.1; 4788 -6.1; 5267 -4.9; 5793 -1.0; 6373 1.7; 7010 0.8; 7711 0.3; 8482 -0.4; 9330 -3.3; 10263 -1.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.44 | 6.7 dB  |
| Peaking | 107 Hz   | 0.71 | -5.6 dB |
| Peaking | 1912 Hz  | 2.08 | -3.8 dB |
| Peaking | 3810 Hz  | 1.36 | -5.2 dB |
| Peaking | 23471 Hz | 2.42 | -3.8 dB |
| Peaking | 260 Hz   | 4.57 | -1.5 dB |
| Peaking | 668 Hz   | 2.23 | 2.7 dB  |
| Peaking | 5171 Hz  | 4.13 | -5.4 dB |
| Peaking | 6134 Hz  | 1.97 | 4.3 dB  |
| Peaking | 9502 Hz  | 6.01 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300%20Rev%202/HiFiMAN%20HE-300%20Rev%202.png)