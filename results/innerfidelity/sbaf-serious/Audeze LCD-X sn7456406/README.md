# Audeze LCD-X sn7456406

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 3.9; 31 2.6; 34 2.2; 37 2.1; 41 1.7; 45 1.6; 49 1.5; 54 1.3; 60 1.3; 66 1.2; 72 0.9; 79 0.8; 87 0.3; 96 -0.1; 106 -0.4; 116 -0.5; 128 -0.9; 141 -1.1; 155 -1.2; 170 -1.4; 187 -1.5; 206 -1.6; 227 -1.3; 249 -1.4; 274 -1.5; 302 -1.5; 332 -1.6; 365 -1.4; 402 -1.3; 442 -1.1; 486 -1.0; 535 -0.7; 588 -0.1; 647 -0.4; 712 -0.4; 783 -0.1; 861 -0.3; 947 -0.1; 1042 0.4; 1146 0.9; 1261 1.2; 1387 -0.1; 1526 -0.3; 1678 -0.6; 1846 -1.0; 2031 -1.2; 2234 -1.6; 2457 0.4; 2703 2.2; 2973 3.3; 3270 4.1; 3597 3.7; 3957 3.4; 4353 1.2; 4788 0.5; 5267 -1.1; 5793 2.6; 6373 2.2; 7010 0.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -2.0; 18182 -2.4; 20000 -1.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X sn7456406 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7456406 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.6  | 9.2 dB  |
| Peaking | 245 Hz   |  0.7  | -1.7 dB |
| Peaking | 3404 Hz  |  3.32 | 4.7 dB  |
| Peaking | 6098 Hz  | 11.35 | 4.1 dB  |
| Peaking | 18269 Hz |  1.42 | -2.5 dB |
| Peaking | 137 Hz   |  3.9  | -0.3 dB |
| Peaking | 1202 Hz  |  6.55 | 1.4 dB  |
| Peaking | 2093 Hz  |  3.33 | -2.5 dB |
| Peaking | 3249 Hz  |  0.73 | 0.7 dB  |
| Peaking | 5210 Hz  |  7.86 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7456406/Audeze%20LCD-X%20sn7456406.png)