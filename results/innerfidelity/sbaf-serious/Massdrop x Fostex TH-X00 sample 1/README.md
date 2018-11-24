# Massdrop x Fostex TH-X00 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.4; 28 -0.4; 31 -0.9; 34 -1.2; 37 -1.4; 41 -1.5; 45 -1.6; 49 -1.6; 54 -1.6; 60 -1.6; 66 -1.8; 72 -2.0; 79 -2.2; 87 -2.4; 96 -2.6; 106 -2.7; 116 -2.6; 128 -2.7; 141 -2.7; 155 -2.7; 170 -2.5; 187 -2.3; 206 -2.0; 227 -1.1; 249 -0.9; 274 -0.7; 302 -0.4; 332 -0.1; 365 0.3; 402 0.6; 442 1.0; 486 1.0; 535 0.9; 588 1.1; 647 2.2; 712 2.1; 783 1.5; 861 1.1; 947 0.3; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.5; 1526 -1.0; 1678 -1.2; 1846 -0.9; 2031 -0.4; 2234 0.2; 2457 1.2; 2703 1.7; 2973 2.0; 3270 3.2; 3597 5.6; 3957 3.8; 4353 2.7; 4788 2.4; 5267 1.0; 5793 0.4; 6373 1.6; 7010 2.1; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.5; 11289 -1.1; 12418 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.58 | 3.7 dB  |
| Peaking | 42 Hz    | 0.43 | -1.8 dB |
| Peaking | 139 Hz   | 1.09 | -2.3 dB |
| Peaking | 658 Hz   | 2.29 | 2.3 dB  |
| Peaking | 3672 Hz  | 2.76 | 5.3 dB  |
| Peaking | 427 Hz   | 4.22 | 0.8 dB  |
| Peaking | 1694 Hz  | 2.26 | -1.5 dB |
| Peaking | 2548 Hz  | 7.23 | 1.0 dB  |
| Peaking | 6803 Hz  | 7.34 | 2.2 dB  |
| Peaking | 10650 Hz | 5.52 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sample%201/Massdrop%20x%20Fostex%20TH-X00%20sample%201.png)