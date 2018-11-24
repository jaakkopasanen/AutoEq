# Audeze LCD-2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 3.5; 28 3.5; 31 3.5; 34 3.5; 37 3.5; 41 3.3; 45 3.1; 49 2.9; 54 2.7; 60 2.4; 66 2.0; 72 1.7; 79 1.5; 87 1.2; 96 0.9; 106 0.7; 116 0.4; 128 0.1; 141 -0.1; 155 -0.3; 170 -0.4; 187 -0.5; 206 -0.7; 227 -0.8; 249 -0.9; 274 -0.9; 302 -0.9; 332 -0.9; 365 -0.9; 402 -0.8; 442 -0.6; 486 -0.7; 535 -0.5; 588 -0.5; 647 -0.8; 712 -1.1; 783 -1.0; 861 -1.2; 947 -0.6; 1042 0.4; 1146 1.2; 1261 1.4; 1387 1.0; 1526 0.4; 1678 1.0; 1846 2.1; 2031 2.4; 2234 2.0; 2457 2.6; 2703 2.8; 2973 3.4; 3270 4.0; 3597 5.3; 3957 6.0; 4353 5.7; 4788 4.4; 5267 4.1; 5793 4.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.4; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.99 | 3.5 dB  |
| Peaking | 51 Hz    | 1.47 | 2.1 dB  |
| Peaking | 2148 Hz  | 1.95 | 1.6 dB  |
| Peaking | 3988 Hz  | 1.95 | 5.9 dB  |
| Peaking | 6195 Hz  | 4.47 | 4.0 dB  |
| Peaking | 94 Hz    | 1.62 | 0.7 dB  |
| Peaking | 376 Hz   | 0.33 | -1.0 dB |
| Peaking | 1203 Hz  | 4.72 | 1.7 dB  |
| Peaking | 19212 Hz | 1.98 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2/Audeze%20LCD-2.png)