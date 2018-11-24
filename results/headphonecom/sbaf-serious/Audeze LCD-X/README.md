# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.6; 28 2.6; 31 2.5; 34 2.3; 37 2.0; 41 1.7; 45 1.4; 49 1.4; 54 1.4; 60 1.0; 66 0.9; 72 0.9; 79 0.4; 87 0.2; 96 0.0; 106 -0.2; 116 -0.4; 128 -0.6; 141 -0.8; 155 -1.0; 170 -1.1; 187 -1.2; 206 -1.2; 227 -1.2; 249 -1.2; 274 -1.3; 302 -1.4; 332 -1.4; 365 -1.2; 402 -0.8; 442 -1.0; 486 -1.0; 535 -0.8; 588 -0.5; 647 -0.4; 712 -0.5; 783 -0.6; 861 -0.5; 947 0.1; 1042 0.0; 1146 0.3; 1261 -0.4; 1387 -0.9; 1526 -1.7; 1678 -2.3; 1846 -1.6; 2031 -1.5; 2234 -2.0; 2457 0.4; 2703 1.6; 2973 2.3; 3270 5.7; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.7; 16529 -3.6; 18182 -5.0; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.4  | 2.7 dB  |
| Peaking | 235 Hz   | 0.55 | -1.5 dB |
| Peaking | 2012 Hz  | 1.7  | -3.8 dB |
| Peaking | 4269 Hz  | 1.06 | 7.3 dB  |
| Peaking | 17959 Hz | 1.6  | -5.4 dB |
| Peaking | 1117 Hz  | 6.8  | 0.8 dB  |
| Peaking | 3389 Hz  | 7.97 | 2.1 dB  |
| Peaking | 4401 Hz  | 1.44 | -1.2 dB |
| Peaking | 6291 Hz  | 2.61 | 4.0 dB  |
| Peaking | 7652 Hz  | 2.39 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)