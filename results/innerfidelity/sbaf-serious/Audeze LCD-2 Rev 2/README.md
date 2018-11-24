# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.5; 28 2.5; 31 2.5; 34 2.5; 37 2.4; 41 2.3; 45 2.4; 49 2.4; 54 2.0; 60 1.2; 66 1.0; 72 0.9; 79 0.7; 87 0.4; 96 0.0; 106 -0.2; 116 -0.4; 128 -0.7; 141 -1.1; 155 -1.4; 170 -1.5; 187 -1.7; 206 -1.8; 227 -1.7; 249 -1.5; 274 -1.4; 302 -1.5; 332 -1.5; 365 -1.5; 402 -1.4; 442 -1.3; 486 -1.5; 535 -1.4; 588 -1.1; 647 -1.6; 712 -1.9; 783 -1.6; 861 -1.3; 947 -0.5; 1042 0.5; 1146 1.7; 1261 1.5; 1387 0.8; 1526 -0.5; 1678 -0.5; 1846 0.6; 2031 0.9; 2234 1.1; 2457 1.7; 2703 1.9; 2973 3.1; 3270 2.6; 3597 4.4; 3957 5.8; 4353 4.7; 4788 2.5; 5267 1.2; 5793 2.2; 6373 1.2; 7010 2.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -4.0; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.64 | 3.0 dB  |
| Peaking | 1163 Hz  | 4.54 | 2.8 dB  |
| Peaking | 3909 Hz  | 3.36 | 4.4 dB  |
| Peaking | 4553 Hz  | 0.31 | 3.6 dB  |
| Peaking | 5174 Hz  | 0    | -2.4 dB |
| Peaking | 57 Hz    | 0.53 | 2.0 dB  |
| Peaking | 402 Hz   | 1.94 | 0.6 dB  |
| Peaking | 2910 Hz  | 6.12 | 0.9 dB  |
| Peaking | 8503 Hz  | 4.82 | -0.8 dB |
| Peaking | 15076 Hz | 3.08 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)