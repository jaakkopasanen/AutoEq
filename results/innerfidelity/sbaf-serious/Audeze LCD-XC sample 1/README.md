# Audeze LCD-XC sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.6; 28 2.8; 31 2.7; 34 2.4; 37 2.1; 41 2.0; 45 2.0; 49 1.9; 54 1.5; 60 1.0; 66 0.6; 72 0.3; 79 -0.0; 87 -0.3; 96 -0.5; 106 -0.7; 116 -0.8; 128 -1.0; 141 -1.2; 155 -1.1; 170 -1.2; 187 -1.2; 206 -1.1; 227 -0.6; 249 -0.2; 274 0.4; 302 0.7; 332 1.1; 365 1.7; 402 2.0; 442 2.1; 486 1.9; 535 2.1; 588 2.3; 647 2.4; 712 2.0; 783 1.7; 861 1.0; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.7; 1387 -2.9; 1526 -3.8; 1678 -4.2; 1846 -3.9; 2031 -2.7; 2234 -1.0; 2457 0.5; 2703 1.9; 2973 2.5; 3270 2.4; 3597 0.3; 3957 -1.2; 4353 1.7; 4788 4.5; 5267 4.7; 5793 4.8; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -3.1; 15026 -2.6; 16529 -2.4; 18182 -5.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  1.22 | 3.0 dB  |
| Peaking | 1699 Hz  |  2.75 | -4.9 dB |
| Peaking | 2900 Hz  |  4.35 | 2.9 dB  |
| Peaking | 5703 Hz  |  2.47 | 5.7 dB  |
| Peaking | 19083 Hz |  0.72 | -5.0 dB |
| Peaking | 175 Hz   |  1.01 | -2.0 dB |
| Peaking | 626 Hz   |  0.63 | 4.1 dB  |
| Peaking | 1581 Hz  |  0.47 | -3.6 dB |
| Peaking | 2194 Hz  |  1.06 | 2.7 dB  |
| Peaking | 4746 Hz  | 11.49 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%201/Audeze%20LCD-XC%20sample%201.png)