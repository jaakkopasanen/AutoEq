# 64 Audio N8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -0.8; 28 -0.8; 31 -0.9; 34 -1.0; 37 -1.1; 41 -1.2; 45 -1.4; 49 -1.5; 54 -1.8; 60 -2.0; 66 -2.4; 72 -2.4; 79 -2.7; 87 -2.8; 96 -2.3; 106 -2.8; 116 -2.6; 128 -2.8; 141 -2.8; 155 -2.7; 170 -2.8; 187 -2.9; 206 -2.9; 227 -2.9; 249 -2.9; 274 -2.9; 302 -2.8; 332 -2.8; 365 -2.6; 402 -2.5; 442 -2.4; 486 -2.2; 535 -2.0; 588 -1.7; 647 -1.4; 712 -1.0; 783 -0.5; 861 -0.1; 947 0.0; 1042 -0.2; 1146 -0.9; 1261 -1.9; 1387 -2.7; 1526 -3.0; 1678 -2.9; 1846 -2.7; 2031 -2.4; 2234 -1.9; 2457 -1.1; 2703 -0.0; 2973 0.9; 3270 1.5; 3597 1.7; 3957 1.3; 4353 0.8; 4788 0.2; 5267 0.7; 5793 4.2; 6373 4.6; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.9; 15026 -4.2; 16529 -1.0; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.43 | -2.7 dB |
| Peaking | 361 Hz   | 1.05 | -1.7 dB |
| Peaking | 1658 Hz  | 2.37 | -3.3 dB |
| Peaking | 6163 Hz  | 4.08 | 5.2 dB  |
| Peaking | 14872 Hz | 3.92 | -4.8 dB |
| Peaking | 938 Hz   | 2.45 | 2.4 dB  |
| Peaking | 966 Hz   | 1.27 | -1.4 dB |
| Peaking | 2268 Hz  | 4.93 | -1.2 dB |
| Peaking | 3410 Hz  | 2.36 | 1.9 dB  |
| Peaking | 5058 Hz  | 8    | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/64%20Audio%20N8/64%20Audio%20N8.png)