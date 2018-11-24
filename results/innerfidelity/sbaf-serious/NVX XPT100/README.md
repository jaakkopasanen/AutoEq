# NVX XPT100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.4; 28 4.9; 31 4.5; 34 4.1; 37 3.9; 41 3.6; 45 3.3; 49 3.1; 54 2.9; 60 2.5; 66 2.3; 72 2.0; 79 1.7; 87 1.4; 96 1.1; 106 1.0; 116 0.9; 128 0.2; 141 -0.6; 155 -1.0; 170 -0.2; 187 -0.9; 206 -0.8; 227 0.1; 249 1.7; 274 4.2; 302 5.6; 332 4.8; 365 3.6; 402 2.8; 442 2.2; 486 1.3; 535 1.0; 588 1.0; 647 0.8; 712 0.6; 783 1.0; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.8; 1526 -2.6; 1678 -2.8; 1846 -3.0; 2031 -2.8; 2234 -2.5; 2457 -1.6; 2703 -1.1; 2973 1.1; 3270 3.2; 3597 0.5; 3957 0.8; 4353 1.8; 4788 3.2; 5267 5.8; 5793 6.0; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.0; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX XPT100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.97 | 5.7 dB  |
| Peaking | 54 Hz    | 1.56 | 1.8 dB  |
| Peaking | 322 Hz   | 2.78 | 5.7 dB  |
| Peaking | 1829 Hz  | 2.17 | -3.6 dB |
| Peaking | 5551 Hz  | 2.71 | 6.4 dB  |
| Peaking | 184 Hz   | 1.57 | -2.4 dB |
| Peaking | 271 Hz   | 0.32 | 0.9 dB  |
| Peaking | 3003 Hz  | 1.79 | -1.6 dB |
| Peaking | 3173 Hz  | 6.74 | 5.0 dB  |
| Peaking | 19719 Hz | 2.66 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100/NVX%20XPT100.png)