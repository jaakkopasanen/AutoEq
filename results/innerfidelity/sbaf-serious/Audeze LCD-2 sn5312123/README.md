# Audeze LCD-2 sn5312123

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.6; 28 1.7; 31 1.8; 34 1.9; 37 2.0; 41 1.9; 45 1.3; 49 0.9; 54 0.9; 60 0.7; 66 0.3; 72 0.1; 79 -0.1; 87 -0.4; 96 -0.8; 106 -1.1; 116 -1.3; 128 -1.6; 141 -2.0; 155 -2.2; 170 -2.3; 187 -2.2; 206 -2.4; 227 -2.6; 249 -2.8; 274 -2.9; 302 -2.7; 332 -2.6; 365 -2.6; 402 -2.4; 442 -2.0; 486 -2.1; 535 -1.6; 588 -1.3; 647 -1.5; 712 -1.8; 783 -1.4; 861 -1.4; 947 -0.5; 1042 0.3; 1146 1.2; 1261 1.0; 1387 0.6; 1526 0.2; 1678 0.7; 1846 1.5; 2031 1.5; 2234 0.9; 2457 1.7; 2703 1.4; 2973 2.1; 3270 2.1; 3597 3.1; 3957 4.1; 4353 3.8; 4788 2.1; 5267 0.8; 5793 0.8; 6373 1.9; 7010 0.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -3.7; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sn5312123 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5312123 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 33 Hz    |  0.63 | 2.1 dB  |
| Peaking | 301 Hz   |  0.42 | -3.4 dB |
| Peaking | 791 Hz   |  2.88 | -1.5 dB |
| Peaking | 1182 Hz  |  0.38 | 1.8 dB  |
| Peaking | 4025 Hz  |  2.76 | 3.5 dB  |
| Peaking | 1158 Hz  |  7.05 | 0.8 dB  |
| Peaking | 1520 Hz  |  7.7  | -1.0 dB |
| Peaking | 6266 Hz  | 13.79 | 1.7 dB  |
| Peaking | 19488 Hz |  1.68 | -5.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5312123/Audeze%20LCD-2%20sn5312123.png)