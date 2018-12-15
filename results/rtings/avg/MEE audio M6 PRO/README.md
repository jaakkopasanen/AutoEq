# MEE audio M6 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.4; 28 1.2; 31 1.0; 34 0.8; 37 0.7; 41 0.6; 45 0.6; 49 0.5; 54 0.3; 60 -0.2; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.6; 96 -2.0; 106 -2.6; 116 -3.0; 128 -3.4; 141 -3.7; 155 -3.9; 170 -3.9; 187 -3.9; 206 -3.7; 227 -3.5; 249 -3.3; 274 -2.9; 302 -2.5; 332 -1.9; 365 -1.4; 402 -1.0; 442 -0.7; 486 -0.3; 535 0.3; 588 0.8; 647 1.1; 712 1.3; 783 1.4; 861 1.0; 947 0.3; 1042 -0.3; 1146 -1.4; 1261 -1.9; 1387 -2.3; 1526 -2.9; 1678 -3.7; 1846 -4.6; 2031 -5.5; 2234 -6.0; 2457 -6.8; 2703 -8.5; 2973 -9.0; 3270 -8.1; 3597 -7.7; 3957 -8.4; 4353 -10.8; 4788 -13.9; 5267 -15.2; 5793 -8.6; 6373 -4.7; 7010 -3.0; 7711 -4.4; 8482 -5.5; 9330 -2.7; 10263 0.0; 11289 0.0; 12418 -0.3; 13660 -2.2; 15026 -1.4; 16529 -1.8; 18182 -2.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 171 Hz   | 1.01 | -4.3 dB  |
| Peaking | 2727 Hz  | 1.31 | -7.2 dB  |
| Peaking | 5046 Hz  | 2.69 | -13.8 dB |
| Peaking | 13981 Hz | 4.49 | -1.6 dB  |
| Peaking | 17776 Hz | 2.4  | -2.8 dB  |
| Peaking | 21 Hz    | 0.98 | 1.8 dB   |
| Peaking | 737 Hz   | 2.57 | 2.4 dB   |
| Peaking | 6754 Hz  | 3.95 | 2.6 dB   |
| Peaking | 8540 Hz  | 2.89 | -5.4 dB  |
| Peaking | 10098 Hz | 2.72 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)