# MEE audio M9B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -13.4; 23 -13.1; 25 -12.6; 28 -11.5; 31 -10.5; 34 -9.8; 37 -9.3; 41 -9.0; 45 -9.0; 49 -9.0; 54 -9.0; 60 -8.8; 66 -8.5; 72 -7.9; 79 -7.1; 87 -6.4; 96 -5.9; 106 -5.6; 116 -5.5; 128 -5.4; 141 -5.2; 155 -5.0; 170 -4.6; 187 -4.4; 206 -4.0; 227 -3.6; 249 -3.0; 274 -2.4; 302 -1.9; 332 -1.2; 365 -0.6; 402 0.1; 442 0.7; 486 1.3; 535 1.9; 588 2.3; 647 2.5; 712 2.3; 783 1.7; 861 0.9; 947 0.2; 1042 0.1; 1146 0.2; 1261 0.2; 1387 -0.1; 1526 -0.3; 1678 -0.3; 1846 0.2; 2031 0.6; 2234 1.1; 2457 1.3; 2703 -0.2; 2973 -2.4; 3270 -4.2; 3597 -4.9; 3957 -4.9; 4353 -5.2; 4788 -4.1; 5267 -3.1; 5793 -4.9; 6373 -10.4; 7010 -8.3; 7711 -3.1; 8482 -2.1; 9330 -7.2; 10263 -9.4; 11289 -2.3; 12418 0.0; 13660 0.0; 15026 -2.2; 16529 -3.9; 18182 -2.6; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M9B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M9B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.16 | -12.9 dB |
| Peaking | 170 Hz   | 1.58 | -2.4 dB  |
| Peaking | 6162 Hz  | 1.37 | -7.2 dB  |
| Peaking | 10058 Hz | 6.8  | -8.5 dB  |
| Peaking | 20344 Hz | 0.92 | -5.7 dB  |
| Peaking | 626 Hz   | 1.91 | 3.1 dB   |
| Peaking | 2452 Hz  | 2.14 | 5.2 dB   |
| Peaking | 3258 Hz  | 1.11 | -4.6 dB  |
| Peaking | 5318 Hz  | 5.82 | 5.0 dB   |
| Peaking | 12568 Hz | 4.32 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/MEE%20audio%20M9B/MEE%20audio%20M9B.png)