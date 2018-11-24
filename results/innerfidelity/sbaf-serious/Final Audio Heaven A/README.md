# Final Audio Heaven A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 4.6; 25 4.3; 28 3.8; 31 3.4; 34 3.1; 37 2.8; 41 2.4; 45 2.1; 49 1.7; 54 1.4; 60 0.9; 66 0.5; 72 0.1; 79 -0.4; 87 -0.8; 96 -1.4; 106 -1.6; 116 -1.9; 128 -2.3; 141 -2.6; 155 -2.7; 170 -2.9; 187 -3.0; 206 -3.1; 227 -3.0; 249 -2.9; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.2; 402 -1.9; 442 -1.4; 486 -1.2; 535 -0.9; 588 -0.3; 647 -0.1; 712 0.0; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.6; 1387 -1.2; 1526 -1.6; 1678 -2.0; 1846 -2.3; 2031 -2.4; 2234 -2.6; 2457 -2.8; 2703 -2.9; 2973 -1.6; 3270 0.8; 3597 3.3; 3957 3.8; 4353 2.6; 4788 1.9; 5267 1.4; 5793 -1.3; 6373 -5.9; 7010 -3.9; 7711 -2.2; 8482 -3.6; 9330 -2.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.47 | 5.0 dB  |
| Peaking | 190 Hz  | 0.65 | -3.4 dB |
| Peaking | 2629 Hz | 1.15 | -8.8 dB |
| Peaking | 3975 Hz | 0.77 | 10.2 dB |
| Peaking | 6601 Hz | 1.53 | -9.1 dB |
| Peaking | 833 Hz  | 2.3  | 1.0 dB  |
| Peaking | 1852 Hz | 1.34 | -1.1 dB |
| Peaking | 2207 Hz | 3.54 | 1.2 dB  |
| Peaking | 8622 Hz | 2.47 | 2.2 dB  |
| Peaking | 8798 Hz | 6.32 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20A/Final%20Audio%20Heaven%20A.png)